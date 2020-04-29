
import common
import eval_tool
import torch
import torch.nn as nn
from dbface import DBFace

def nms(objs, iou=0.5):

    if objs is None or len(objs) <= 1:
        return objs

    objs = sorted(objs, key=lambda obj: obj.score, reverse=True)
    keep = []
    flags = [0] * len(objs)
    for index, obj in enumerate(objs):

        if flags[index] != 0:
            continue

        keep.append(obj)
        for j in range(index + 1, len(objs)):
            if flags[j] == 0 and obj.iou(objs[j]) > iou:
                flags[j] = 1
    return keep


mean = [0.408, 0.447, 0.47]
std = [0.289, 0.274, 0.278]

trial_name = "small-H-dense-wide64-UCBA-keep12-ignoresmall"
jobdir = f"jobs/{trial_name}"

image = common.imread("imgs/selfie.jpg")
model = DBFace(has_landmark=True, wide=64, has_ext=True, upmode="UCBA")
model.load(f"{jobdir}/models/150.pth")
model.eval()
model.cuda()

outs = eval_tool.detect_image(model, image, mean, std, 0.2)
outs = nms(outs, 0.2)
print("objs = %d" % len(outs))
for obj in outs:
    common.drawbbox(image, obj)

common.imwrite("test_result/test.jpg", image)
print("ok")