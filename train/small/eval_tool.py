

import numpy as np
import common
import torch.nn as nn
import torch
import json
import cv2
import torch.nn.functional as F

def _nms(heat, kernel=1):
    pad = (kernel - 1) // 2

    hmax = nn.functional.max_pool2d(heat, (kernel, kernel), stride=1, padding=pad)
    keep = (hmax == heat).float()
    return heat * keep
    # hmax = heat
    # return hmax


def _topk(scores, K=20):
    batch, cat, height, width = scores.size()

    topk_scores, topk_inds = torch.topk(scores.view(batch, -1), K)
    topk_clses = (topk_inds / (height * width)).int()

    topk_inds = topk_inds % (height * width)
    topk_ys   = (topk_inds / width).int().float()
    topk_xs   = (topk_inds % width).int().float()
    return topk_scores, topk_inds, topk_clses, topk_ys, topk_xs


def detect_images_giou_with_netout(output_hm, output_tlrb, output_landmark, threshold=0.4, ibatch=0):

    stride = 4
    _, num_classes, hm_height, hm_width = output_hm.shape
    hm = output_hm[ibatch].reshape(1, num_classes, hm_height, hm_width)
    tlrb = output_tlrb[ibatch].cpu().data.numpy().reshape(1, num_classes * 4, hm_height, hm_width)
    landmark = output_landmark[ibatch].cpu().data.numpy().reshape(1, num_classes * 10, hm_height, hm_width)

    nmskey = _nms(hm, 3)
    kscore, kinds, kcls, kys, kxs = _topk(nmskey, 2000)
    kys = kys.cpu().data.numpy().astype(np.int)
    kxs = kxs.cpu().data.numpy().astype(np.int)
    kcls = kcls.cpu().data.numpy().astype(np.int)

    key = [[], [], [], []]
    for ind in range(kscore.shape[1]):
        score = kscore[0, ind]
        if score > threshold:
            key[0].append(kys[0, ind])
            key[1].append(kxs[0, ind])
            key[2].append(score)
            key[3].append(kcls[0, ind])

    imboxs = []
    if key[0] is not None and len(key[0]) > 0:
        ky, kx = key[0], key[1]
        classes = key[3]
        scores = key[2]

        for i in range(len(kx)):
            class_ = classes[i]
            cx, cy = kx[i], ky[i]
            x1, y1, x2, y2 = tlrb[0, class_*4:(class_+1)*4, cy, cx]
            x1, y1, x2, y2 = (np.array([cx, cy, cx, cy]) + np.array([-x1, -y1, x2, y2])) * stride

            x5y5 = landmark[0, 0:10, cy, cx]
            x5y5 = np.array(common.exp(x5y5 * 4))
            x5y5 = (x5y5 + np.array([cx]*5 + [cy]*5)) * stride
            boxlandmark = list(zip(x5y5[:5], x5y5[5:]))
            imboxs.append(common.BBox(label=str(class_), xyrb=common.floatv([x1, y1, x2, y2]), score=scores[i].item(), landmark=boxlandmark))
    return imboxs


def detect_images_giou_with_retinaface_style_eval(output_hm, output_tlrb, output_landmark, threshold=0.4, ibatch=0):

    stride = 4
    _, _, hm_height, hm_width = output_hm.shape
    hm = output_hm[ibatch].reshape(1, 1, hm_height, hm_width)
    tlrb = output_tlrb[ibatch]
    landmark = output_landmark[ibatch]

    area = hm_height * hm_width
    keep = (hm > threshold).view(area)
    indices = torch.arange(0, area)[keep]
    hm = hm.view(1, area).cpu().data.numpy()
    tlrb = tlrb.view(4, area).cpu().data.numpy()
    landmark = landmark.view(10, area).cpu().data.numpy()

    cx, cy = indices % hm_width, indices // hm_width
    scores = hm[0, indices]
    x1, y1, x2, y2 = tlrb[0:4, indices]
    cts = np.vstack([cx, cy, cx, cy])
    locs = np.vstack([-x1, -y1, x2, y2])
    x1, y1, x2, y2 = (cts + locs) * stride

    x5y5 = landmark[0:10, indices]
    x5y5 = common.exp(x5y5 * 4)
    x5y5 = (x5y5 + np.vstack([cx] * 5 + [cy] * 5)) * stride

    imboxs = []
    for i in range(len(indices)):
        boxlandmark = list(zip(x5y5[0:5, i], x5y5[5:, i]))
        imboxs.append(common.BBox(label="facial", xyrb=common.floatv([x1[i], y1[i], x2[i], y2[i]]), score=scores[i], landmark=boxlandmark))
    return imboxs


def detect_image(model, image, mean, std, threshold=0.4):
    image = common.pad(image)
    image = ((image / 255 - mean) / std).astype(np.float32)
    image = image.transpose(2, 0, 1)
    image = torch.from_numpy(image).unsqueeze(0).cuda()
    center, box, landmark = model(image)

    center = center.sigmoid()
    box = torch.exp(box)
    # debug
    # center = F.max_pool2d(center, kernel_size=3, padding=1, stride=1)
    return detect_images_giou_with_netout(center, box, landmark, threshold)


def detect_image_retinaface_style(model, image, mean, std, threshold=0.4):
    image = common.pad(image)
    image = ((image / 255 - mean) / std).astype(np.float32)
    image = image.transpose(2, 0, 1)
    image = torch.from_numpy(image).unsqueeze(0).cuda()
    center, box, landmark = model(image)

    center = center.sigmoid()
    box = torch.exp(box)
    return detect_images_giou_with_retinaface_style_eval(center, box, landmark, threshold)