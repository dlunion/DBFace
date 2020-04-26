#-*-coding:utf-8-*-
from __future__ import division
"""
WiderFace evaluation code
author: wondervictor
mail: tianhengcheng@gmail.com
copyright@wondervictor
"""
import os
import tqdm
import pickle
import argparse
import numpy as np
from scipy.io import loadmat
from evaluate.bbox import bbox_overlaps
from IPython import embed


def get_gt_boxes(gt_dir):
    """ gt dir: (wider_face_val.mat, wider_easy_val.mat, wider_medium_val.mat, wider_hard_val.mat)"""

    gt_mat = loadmat(os.path.join(gt_dir, 'wider_face_val.mat'))
    hard_mat = loadmat(os.path.join(gt_dir, 'wider_hard_val.mat'))
    medium_mat = loadmat(os.path.join(gt_dir, 'wider_medium_val.mat'))
    easy_mat = loadmat(os.path.join(gt_dir, 'wider_easy_val.mat'))

    facebox_list = gt_mat['face_bbx_list']
    event_list = gt_mat['event_list']
    file_list = gt_mat['file_list']

    hard_gt_list = hard_mat['gt_list']
    medium_gt_list = medium_mat['gt_list']
    easy_gt_list = easy_mat['gt_list']

    return facebox_list, event_list, file_list, hard_gt_list, medium_gt_list, easy_gt_list


def get_gt_boxes_from_txt(gt_path, cache_dir):

    cache_file = os.path.join(cache_dir, 'gt_cache.pkl')
    if os.path.exists(cache_file):
        f = open(cache_file, 'rb')
        boxes = pickle.load(f)
        f.close()
        return boxes

    f = open(gt_path, 'r')
    state = 0
    lines = f.readlines()
    lines = list(map(lambda x: x.rstrip('\r\n'), lines))
    boxes = {}
    f.close()
    current_boxes = []
    current_name = None
    for line in lines:
        if state == 0 and '--' in line:
            state = 1
            current_name = line
            continue
        if state == 1:
            state = 2
            continue

        if state == 2 and '--' in line:
            state = 1
            boxes[current_name] = np.array(current_boxes).astype('float32')
            current_name = line
            current_boxes = []
            continue

        if state == 2:
            box = [float(x) for x in line.split(' ')[:4]]
            current_boxes.append(box)
            continue

    f = open(cache_file, 'wb')
    pickle.dump(boxes, f)
    f.close()
    return boxes


def read_pred_file(filepath):

    with open(filepath, 'r') as f:
        lines = f.readlines()
        img_file = lines[0].rstrip('\n\r')
        lines = lines[2:]

    boxes = np.array(list(map(lambda x: [float(a) for a in x.rstrip('\r\n').split(' ')], lines))).astype('float')
    return img_file.split('/')[-1], boxes


def get_preds(pred_dir):
    events = os.listdir(pred_dir)
    boxes = dict()
    pbar = tqdm.tqdm(events)

    for event in pbar:
        pbar.set_description('Reading Predictions ')
        event_dir = os.path.join(pred_dir, event)
        event_images = os.listdir(event_dir)
        current_event = dict()
        for imgtxt in event_images:
            imgname, _boxes = read_pred_file(os.path.join(event_dir, imgtxt))
            current_event[imgname.rstrip('.jpg')] = _boxes
        boxes[event] = current_event
    return boxes


def norm_score(pred):
    """ norm score
    pred {key: [[x1,y1,x2,y2,s]]}
    """

    max_score = 0
    min_score = 1

    for _, k in pred.items():
        for _, v in k.items():
            if len(v) == 0:
                continue
            _min = np.min(v[:, -1])
            _max = np.max(v[:, -1])
            max_score = max(_max, max_score)
            min_score = min(_min, min_score)

    diff = max_score - min_score
    for _, k in pred.items():
        for _, v in k.items():
            if len(v) == 0:
                continue
            v[:, -1] = (v[:, -1] - min_score)/diff


def image_eval(pred, gt, ignore, iou_thresh):
    """ single image evaluation
    pred: Nx5
    gt: Nx4
    ignore:
    """
    _pred = pred.copy()
    _gt = gt.copy()
    pred_recall = np.zeros(_pred.shape[0])
    recall_list = np.zeros(_gt.shape[0])
    proposal_list = np.ones(_pred.shape[0])

    _pred[:, 2] = _pred[:, 2] + _pred[:, 0]
    _pred[:, 3] = _pred[:, 3] + _pred[:, 1]
    _gt[:, 2] = _gt[:, 2] + _gt[:, 0]
    _gt[:, 3] = _gt[:, 3] + _gt[:, 1]

    overlaps = bbox_overlaps(_pred[:, :4], _gt)

    for h in range(_pred.shape[0]):

        gt_overlap = overlaps[h]
        max_overlap, max_idx = gt_overlap.max(), gt_overlap.argmax()
        if max_overlap >= iou_thresh:
            if ignore[max_idx] == 0:
                recall_list[max_idx] = -1
                proposal_list[h] = -1
            elif recall_list[max_idx] == 0:
                recall_list[max_idx] = 1

        r_keep_index = np.where(recall_list == 1)[0]
        pred_recall[h] = len(r_keep_index)
    return pred_recall, proposal_list


def img_pr_info(thresh_num, pred_info, proposal_list, pred_recall):
    pr_info = np.zeros((thresh_num, 2)).astype('float')
    for t in range(thresh_num):

        thresh = 1 - (t+1)/thresh_num
        r_index = np.where(pred_info[:, 4] >= thresh)[0]
        if len(r_index) == 0:
            pr_info[t, 0] = 0
            pr_info[t, 1] = 0
        else:
            r_index = r_index[-1]
            p_index = np.where(proposal_list[:r_index+1] == 1)[0]
            pr_info[t, 0] = len(p_index)
            pr_info[t, 1] = pred_recall[r_index]
    return pr_info


def dataset_pr_info(thresh_num, pr_curve, count_face):
    _pr_curve = np.zeros((thresh_num, 2))
    for i in range(thresh_num):
        _pr_curve[i, 0] = pr_curve[i, 1] / pr_curve[i, 0]
        _pr_curve[i, 1] = pr_curve[i, 1] / count_face
    return _pr_curve


def voc_ap(rec, prec):

    # correct AP calculation
    # first append sentinel values at the end
    mrec = np.concatenate(([0.], rec, [1.]))
    mpre = np.concatenate(([0.], prec, [0.]))

    # compute the precision envelope
    for i in range(mpre.size - 1, 0, -1):
        mpre[i - 1] = np.maximum(mpre[i - 1], mpre[i])

    # to calculate area under PR curve, look for points
    # where X axis (recall) changes value
    i = np.where(mrec[1:] != mrec[:-1])[0]

    # and sum (\Delta recall) * prec
    ap = np.sum((mrec[i + 1] - mrec[i]) * mpre[i + 1])
    return ap


def eval_map(pred, all, iou_thresh=0.5, gt_path="evaluate/ground_truth"):
    norm_score(pred)
    facebox_list, event_list, file_list, hard_gt_list, medium_gt_list, easy_gt_list = get_gt_boxes(gt_path)
    event_num = len(event_list)
    thresh_num = 1000
    settings = ['easy', 'medium', 'hard']
    setting_gts = [easy_gt_list, medium_gt_list, hard_gt_list]
    
    if not all:
        aps = []
        for setting_id in range(3):
            # different setting
            gt_list = setting_gts[setting_id]
            count_face = 0
            pr_curve = np.zeros((thresh_num, 2)).astype('float')
            # [hard, medium, easy]
            pbar = tqdm.tqdm(range(event_num))  #  61
            error_count = 0
            for i in pbar:
                pbar.set_description('Processing {}'.format(settings[setting_id]))
                event_name = str(event_list[i][0][0])
                img_list = file_list[i][0]

                pred_list = pred[event_name]  
                sub_gt_list = gt_list[i][0]
                print("shape of sub_gt_list is: ",sub_gt_list.shape)
                gt_bbx_list = facebox_list[i][0]

                for j in range(len(img_list)):
                    try:
                        pred_info = pred_list[str(img_list[j][0][0])] 
                    except:
                        error_count+=1
                        continue

                    gt_boxes = gt_bbx_list[j][0].astype('float')
                    keep_index = sub_gt_list[j][0]
                    count_face += len(keep_index)
                    if len(gt_boxes) == 0 or len(pred_info) == 0:
                        continue
                    ignore = np.zeros(gt_boxes.shape[0])
                    if len(keep_index) != 0:
                        ignore[keep_index-1] = 1
                    pred_recall, proposal_list = image_eval(pred_info, gt_boxes, ignore, iou_thresh)

                    _img_pr_info = img_pr_info(thresh_num, pred_info, proposal_list, pred_recall)

                    pr_curve += _img_pr_info
            print("error_count is: ",error_count)
            pr_curve = dataset_pr_info(thresh_num, pr_curve, count_face)

            propose = pr_curve[:, 0]
            recall = pr_curve[:, 1]

            ap = voc_ap(recall, propose)
            aps.append(ap)
        return aps
    else:
        aps = []
        # different setting
        count_face = 0
        pr_curve = np.zeros((thresh_num, 2)).astype('float')  #  control calcultate how many samples
        # [hard, medium, easy]
        pbar = tqdm.tqdm(range(event_num))
        error_count = 0
        for i in pbar:
            pbar.set_description('Processing {}'.format("all"))
            # print("event_list is: ",event_list)
            event_name = str(event_list[i][0][0])  #  '0--Parade', '1--Handshaking'
            img_list = file_list[i][0]
            pred_list = pred[event_name]  #  每个文件夹的所有检测结果
            sub_gt_list = [ setting_gts[0][i][0], setting_gts[1][i][0], setting_gts[2][i][0] ]

            gt_bbx_list = facebox_list[i][0]
            for j in range(len(img_list)):
                try:
                    pred_info = pred_list[str(img_list[j][0][0])]  #   # str(img_list[j][0][0] 是每个folder下面的图片名字
                except:
                    error_count+=1
                    continue

                gt_boxes = gt_bbx_list[j][0].astype('float')
                temp_i = []
                for ii in range(3):
                    if len(sub_gt_list[ii][j][0])!=0:
                        temp_i.append(ii)
                if len(temp_i)!=0:
                    keep_index = np.concatenate(tuple([sub_gt_list[xx][j][0] for xx in temp_i]))
                else:
                    keep_index = []
                count_face += len(keep_index)

                if len(gt_boxes) == 0 or len(pred_info) == 0:
                    continue
                ignore = np.zeros(gt_boxes.shape[0]) # #  no ignore
                if len(keep_index) != 0:
                    ignore[keep_index-1] = 1
                pred_recall, proposal_list = image_eval(pred_info, gt_boxes, ignore, iou_thresh)

                _img_pr_info = img_pr_info(thresh_num, pred_info, proposal_list, pred_recall)

                pr_curve += _img_pr_info

        pr_curve = dataset_pr_info(thresh_num, pr_curve, count_face)

        propose = pr_curve[:, 0]
        recall = pr_curve[:, 1]

        ap = voc_ap(recall, propose)
        aps.append(ap)
        return aps        

