
import common
import eval_tool
import torch
import torch.nn as nn
import torch.nn.functional as F
from dbface import DBFace
import torch.onnx.symbolic_opset11

trial_name = "small-H-dense-wide64-UCBA-keep12-noext"
jobdir = f"jobs/{trial_name}"


class OnnxModel(nn.Module):
    def __init__(self, **kwargs):
        super(OnnxModel, self).__init__()

        self.model = DBFace(**kwargs)
        self.model.load(f"{jobdir}/models/150.pth")

    def forward(self, x):
        center, box, landmark = self.model(x)
        center_sigmoid = torch.sigmoid(center)
        center_maxpool = F.max_pool2d(center_sigmoid, kernel_size=3, padding=1, stride=1)
        box = torch.exp(box)
        return center_sigmoid, center_maxpool, box, landmark

model = OnnxModel(has_landmark=True, wide=64, has_ext=False, upmode="UCBA")
model.eval()
model.cuda()

common.mkdirs_from_file_path(f"{jobdir}/model.onnx")

dummy = torch.zeros((1, 3, 32, 32)).cuda()
torch.onnx.export(model, dummy, f"{jobdir}/model.onnx", output_names=["hm", "pool_hm", "tlrb", "landmark"], opset_version=11)