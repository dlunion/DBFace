
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "3"


import common
import eval_tool
import torch
import torch.nn as nn
import logger
import numpy as np
from dbface import DBFace
from evaluate import evaluation

# create logger
trial_name = "small-H-dense-wide64-UCBA-keep12-noext-ignoresmall2"
jobdir = f"jobs/{trial_name}"
log = logger.create(trial_name, f"{jobdir}/logs/eval.log")

# load and init model
model = DBFace(has_landmark=True, wide=64, has_ext=False, upmode="UCBA")
model.load(f"{jobdir}/models/150.pth")
model.eval()
model.cuda()

# load dataset
mean = [0.408, 0.447, 0.47]
std = [0.289, 0.274, 0.278]
files, anns = zip(*common.load_webface("webface/val/label.txt", "webface/WIDER_val/images"))

# forward and summary
prefix = "webface/WIDER_val/images/"
all_result_dict = {}
total_file = len(files)

for i in range(total_file):

    # preper key and file_name
    file = files[i]
    key = file[len(prefix) : file.rfind("/")]
    file_name = common.file_name_no_suffix(file)

    # load image and forward
    image = common.imread(file)
    objs = eval_tool.detect_image(model, image, mean, std, 0.01)
    #objs = eval_tool.detect_image_retinaface_style(model, image, mean, std, 0.05)
    #objs = common.nms(objs, 0.3)
    
    # summary to all_result_dict
    image_pred = []
    for obj in objs:
        image_pred.append(obj.xywh + [obj.score])

    # build all_result_dict
    if key not in all_result_dict:
        all_result_dict[key] = {}

    all_result_dict[key][file_name] = np.array(image_pred)
    log.info("{} / {}".format(i+1, total_file))

    # write matlab format
    path = f"{jobdir}/matlab_eval_{trial_name}/{key}/{file_name}.txt"
    common.mkdirs_from_file_path(path)

    with open(path, "w") as f:
        f.write(f"/{key}/{file_name}\n{len(image_pred)}\n")

        for item in image_pred:
            f.write("{} {} {} {} {}\n".format(*item))


# eval map of IoU0.5
aps = evaluation.eval_map(all_result_dict, all=False)

log.info("\n"
    "Easy:      {}\n"
    "Medium:    {}\n"
    "Hard:      {}".format(*aps)
)