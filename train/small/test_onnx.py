import onnxruntime
import numpy as np 
import common
import eval_tool
import torch
import torch.nn as nn
from dbface import DBFace
import torch.nn.functional as F

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

trial_name = "small-H-dense-wide64-UCBA-keep12-noext-ignoresmall2"
jobdir = f"jobs/{trial_name}"

image = common.imread("imgs/selfie.jpg")
model = DBFace(has_landmark=True, wide=64, has_ext=False, upmode="UCBA")
model.load(f"{jobdir}/models/150.pth")
model.eval()
model.cuda()

# preprocess
image = common.pad(image)
image = ((image / 255 - mean) / std).astype(np.float32)
image = image.transpose(2, 0, 1)
image = torch.from_numpy(image).unsqueeze(0).cuda()

# pytorch 
center, box, landmark = model(image)
center = center.sigmoid()
box = torch.exp(box)
center = F.max_pool2d(center, kernel_size=3, padding=1, stride=1)
    
# onnxruntime
ort_session = onnxruntime.InferenceSession(f"{jobdir}/model.onnx")

def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

# compute ONNX Runtime output prediction
ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(image)}
ort_outs = ort_session.run(None, ort_inputs)


# compare ONNX Runtime and PyTorch results
np.testing.assert_allclose(to_numpy(center), ort_outs[0], rtol=1e-03, atol=1e-05)
np.testing.assert_allclose(to_numpy(box),    ort_outs[1], rtol=1e-03, atol=1e-05)
np.testing.assert_allclose(to_numpy(landmark), ort_outs[2], rtol=1e-03, atol=1e-05)
print("Exported model has been tested with ONNXRuntime, and the result looks good!")