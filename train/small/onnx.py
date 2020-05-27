import common
import eval_tool
import torch
import torch.nn as nn
import torch.nn.functional as F
from dbface import DBFace
# import torch.onnx.symbolic_opset11
# import torch.onnx.symbolic_helper

trial_name = "small-H-dense-wide64-UCBA-keep12-noext-ignoresmall2"
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
        return center_maxpool, box, landmark

model = OnnxModel(has_landmark=True, wide=64, has_ext=False, upmode="UCBA")

model.eval()
model.cuda()

common.mkdirs_from_file_path(f"{jobdir}/model.onnx")

# dummy = torch.zeros((1, 3, 1152, 2048)).cuda()
dummy = torch.zeros((1, 3, 32, 32)).cuda()
# torch.onnx.export(model, dummy, f"{jobdir}/model.onnx", output_names=["hm", "pool_hm", "tlrb", "landmark"], opset_version=9, verbose=True,)
# torch.onnx.export(model, dummy, f"{jobdir}/model.onnx", output_names=["hm", "pool_hm", "tlrb", "landmark"], opset_version=11, verbose=True)
# torch.onnx.export(model, dummy, f"{jobdir}/model.onnx", opset_version=11, verbose=True, output_names=["hm", "pool_hm", "tlrb", "landmark"], )
torch.onnx._export(model, dummy, f"{jobdir}/model.onnx", export_params=True, verbose=True, output_names=["pool_hm", "tlrb", "landmark"])



