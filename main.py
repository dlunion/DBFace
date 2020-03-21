
import common
import numpy as np
import torch
import torch.nn.functional as F
import torch.nn as nn
from DBFace import DBFace

HAS_CUDA = torch.cuda.is_available()
print(f"HAS_CUDA = {HAS_CUDA}")


def detect(model, image, threshold=0.3):

    mean = [0.408, 0.447, 0.47]
    std = [0.289, 0.274, 0.278]

    image = common.pad(image)
    image = ((image / 255.0 - mean) / std).astype(np.float32)
    image = image.transpose(2, 0, 1)

    torch_image = torch.from_numpy(image)[None]
    if HAS_CUDA:
        torch_image = torch_image.cuda()

    hm, box, landmark = model(torch_image)
    hm_pool = F.max_pool2d(hm, 3, 1, 1)
    scores, indices = ((hm == hm_pool).float() * hm).view(1, -1).cpu().topk(1000)
    hm_height, hm_width = hm.shape[2:]

    scores = scores.squeeze()
    indices = indices.squeeze()
    ys = list((indices / hm_width).int().data.numpy())
    xs = list((indices % hm_width).int().data.numpy())
    scores = list(scores.data.numpy())
    box = box.cpu().squeeze().data.numpy()
    landmark = landmark.cpu().squeeze().data.numpy()

    stride = 4
    objs = []
    for cx, cy, score in zip(xs, ys, scores):
        if score < threshold:
            break

        x, y, r, b = box[:, cy, cx]
        xyrb = (np.array([cx, cy, cx, cy]) + [-x, -y, r, b]) * stride
        x5y5 = landmark[:, cy, cx]
        x5y5 = (common.exp(x5y5 * 4) + ([cx]*5 + [cy]*5)) * stride
        box_landmark = list(zip(x5y5[:5], x5y5[5:]))
        objs.append(common.BBox(0, xyrb=xyrb, score=score, landmark=box_landmark))
    return objs


def detect_image(model, file):

    image = common.imread(file)
    objs = detect(dbface, image)

    for obj in objs:
        common.drawbbox(image, obj)

    common.imwrite("detect_result/" + common.file_name_no_suffix(file) + ".draw.jpg", image)


if __name__ == "__main__":

    
    dbface = DBFace()
    dbface.eval()

    if HAS_CUDA:
        dbface.cuda()

    dbface.load("dbface.pth")

    detect_image(dbface, "imgs/selfie.jpg")
    detect_image(dbface, "imgs/12_Group_Group_12_Group_Group_12_249.jpg")
    detect_image(dbface, "imgs/12_Group_Group_12_Group_Group_12_728.jpg")


    