
import common
import losses
import augment
import numpy as np
import math
import logger
import eval_tool

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms.functional as T
from torch.utils.data import Dataset, DataLoader
from dbface import DBFace


class LDataset(Dataset):
    def __init__(self, labelfile, imagesdir, mean, std, width=800, height=800):
        
        self.width = width
        self.height = height
        self.items = common.load_webface(labelfile, imagesdir)
        self.mean = mean
        self.std = std

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        imgfile, objs = self.items[index]
        image = common.imread(imgfile)

        if image is None:
            log.info("{} is empty, index={}".format(imgfile, index))
            return self[random.randint(0, len(self.items)-1)]

        keepsize            = 12
        image, objs = augment.webface(image, objs, self.width, self.height, keepsize=0)

        # norm
        image = ((image / 255.0 - self.mean) / self.std).astype(np.float32)

        posweight_radius    = 2
        stride              = 4
        fm_width            = self.width // stride
        fm_height           = self.height // stride

        heatmap_gt          = np.zeros((1,     fm_height, fm_width), np.float32)
        heatmap_posweight   = np.zeros((1,     fm_height, fm_width), np.float32)
        keep_mask           = np.ones((1,     fm_height, fm_width), np.float32)
        reg_tlrb            = np.zeros((1 * 4, fm_height, fm_width), np.float32)
        reg_mask            = np.zeros((1,     fm_height, fm_width), np.float32)
        distance_map        = np.zeros((1,     fm_height, fm_width), np.float32) + 1000
        landmark_gt         = np.zeros((1 * 10,fm_height, fm_width), np.float32)
        landmark_mask       = np.zeros((1,     fm_height, fm_width), np.float32)

        hassmall = False
        for obj in objs:
            isSmallObj = obj.area < keepsize * keepsize

            if isSmallObj:
                cx, cy = obj.safe_scale_center(1 / stride, fm_width, fm_height)
                keep_mask[0, cy, cx] = 0
                w, h = obj.width / stride, obj.height / stride

                x0 = int(common.clip_value(cx - w // 2, fm_width-1))
                y0 = int(common.clip_value(cy - h // 2, fm_height-1))
                x1 = int(common.clip_value(cx + w // 2, fm_width-1) + 1)
                y1 = int(common.clip_value(cy + h // 2, fm_height-1) + 1)
                if x1 - x0 > 0 and y1 - y0 > 0:
                    keep_mask[0, y0:y1, x0:x1] = 0
                hassmall = True

        for obj in objs:

            classes = 0
            cx, cy = obj.safe_scale_center(1 / stride, fm_width, fm_height)
            reg_box = np.array(obj.box) / stride
            isSmallObj = obj.area < keepsize * keepsize

            if isSmallObj:
                if obj.area >= 5 * 5:
                    distance_map[classes, cy, cx] = 0
                    reg_tlrb[classes*4:(classes+1)*4, cy, cx] = reg_box
                    reg_mask[classes, cy, cx] = 1
                continue

            w, h = obj.width / stride, obj.height / stride
            x0 = int(common.clip_value(cx - w // 2, fm_width-1))
            y0 = int(common.clip_value(cy - h // 2, fm_height-1))
            x1 = int(common.clip_value(cx + w // 2, fm_width-1) + 1)
            y1 = int(common.clip_value(cy + h // 2, fm_height-1) + 1)
            if x1 - x0 > 0 and y1 - y0 > 0:
                keep_mask[0, y0:y1, x0:x1] = 1

            w_radius, h_radius = common.truncate_radius((obj.width, obj.height))
            gaussian_map = common.draw_truncate_gaussian(heatmap_gt[classes, :, :], (cx, cy), h_radius, w_radius)

            mxface = 300
            miface = 25
            mxline = max(obj.width, obj.height)
            gamma = (mxline - miface) / (mxface - miface) * 10
            gamma = min(max(0, gamma), 10) + 1
            common.draw_gaussian(heatmap_posweight[classes, :, :], (cx, cy), posweight_radius, k=gamma)

            range_expand_x = math.ceil(w_radius)
            range_expand_y = math.ceil(h_radius)

            min_expand_size = 3
            range_expand_x = max(min_expand_size, range_expand_x)
            range_expand_y = max(min_expand_size, range_expand_y)

            icx, icy = cx, cy
            reg_landmark = None
            fill_threshold = 0.3
			
            if obj.haslandmark:
                reg_landmark = np.array(obj.x5y5_cat_landmark) / stride
                x5y5 = [cx]*5 + [cy]*5
                rvalue = (reg_landmark - x5y5)
                landmark_gt[0:10, cy, cx] = np.array(common.log(rvalue)) / 4
                landmark_mask[0, cy, cx] = 1

            if not obj.rotate:
                for cx in range(icx - range_expand_x, icx + range_expand_x + 1):
                    for cy in range(icy - range_expand_y, icy + range_expand_y + 1):
                        if cx < fm_width and cy < fm_height and cx >= 0 and cy >= 0:
                            
                            my_gaussian_value = 0.9
                            gy, gx = cy - icy + range_expand_y, cx - icx + range_expand_x
                            if gy >= 0 and gy < gaussian_map.shape[0] and gx >= 0 and gx < gaussian_map.shape[1]:
                                my_gaussian_value = gaussian_map[gy, gx]
                                
                            distance = math.sqrt((cx - icx)**2 + (cy - icy)**2)
                            if my_gaussian_value > fill_threshold or distance <= min_expand_size:
                                already_distance = distance_map[classes, cy, cx]
                                my_mix_distance = (1 - my_gaussian_value) * distance

                                if my_mix_distance > already_distance:
                                    continue

                                distance_map[classes, cy, cx] = my_mix_distance
                                reg_tlrb[classes*4:(classes+1)*4, cy, cx] = reg_box
                                reg_mask[classes, cy, cx] = 1

        # if hassmall:
        #     common.imwrite("test_result/keep_mask.jpg", keep_mask[0]*255)
        #     common.imwrite("test_result/heatmap_gt.jpg", heatmap_gt[0]*255)
        #     common.imwrite("test_result/keep_ori.jpg", (image*self.std+self.mean)*255)
        return T.to_tensor(image), heatmap_gt, heatmap_posweight, reg_tlrb, reg_mask, landmark_gt, landmark_mask, len(objs), keep_mask



class App(object):
    def __init__(self, labelfile, imagesdir):

        self.width, self.height = 800, 800
        self.mean = [0.408, 0.447, 0.47]
        self.std = [0.289, 0.274, 0.278]
        self.batch_size = 18
        self.lr = 1e-4
        self.gpus = [1] #[0, 1, 2, 3]
        self.gpu_master = self.gpus[0]
        self.model = DBFace(has_landmark=True, wide=64, has_ext=False, upmode="UCBA")
        self.model.init_weights()
        self.model = nn.DataParallel(self.model, device_ids=self.gpus)
        self.model.cuda(device=self.gpu_master)
        self.model.train()

        self.focal_loss = losses.FocalLoss()
        self.giou_loss = losses.GIoULoss()
        self.landmark_loss = losses.WingLoss(w=2)
        self.train_dataset = LDataset(labelfile, imagesdir, mean=self.mean, std=self.std, width=self.width, height=self.height)
        self.train_loader = DataLoader(dataset=self.train_dataset, batch_size=self.batch_size, shuffle=True, num_workers=32)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=self.lr)
        self.per_epoch_batchs = len(self.train_loader)
        self.iter = 0
        self.epochs = 150


    def set_lr(self, lr):

        self.lr = lr
        log.info(f"setting learning rate to: {lr}")
        for param_group in self.optimizer.param_groups:
            param_group["lr"] = lr


    def train_epoch(self, epoch):
        
        for indbatch, (images, heatmap_gt, heatmap_posweight, reg_tlrb, reg_mask, landmark_gt, landmark_mask, num_objs, keep_mask) in enumerate(self.train_loader):

            self.iter += 1

            batch_objs = sum(num_objs)
            batch_size = self.batch_size

            if batch_objs == 0:
                batch_objs = 1

            heatmap_gt          = heatmap_gt.to(self.gpu_master)
            heatmap_posweight   = heatmap_posweight.to(self.gpu_master)
            keep_mask           = keep_mask.to(self.gpu_master)
            reg_tlrb            = reg_tlrb.to(self.gpu_master)
            reg_mask            = reg_mask.to(self.gpu_master)
            landmark_gt         = landmark_gt.to(self.gpu_master)
            landmark_mask       = landmark_mask.to(self.gpu_master)
            images              = images.to(self.gpu_master)

            hm, tlrb, landmark  = self.model(images)
            hm = hm.sigmoid()
            hm = torch.clamp(hm, min=1e-4, max=1-1e-4)
            tlrb = torch.exp(tlrb)

            hm_loss = self.focal_loss(hm, heatmap_gt, heatmap_posweight, keep_mask=keep_mask) / batch_objs
            reg_loss = self.giou_loss(tlrb, reg_tlrb, reg_mask)*5
            landmark_loss = self.landmark_loss(landmark, landmark_gt, landmark_mask)*0.1
            loss = hm_loss + reg_loss + landmark_loss

            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

            epoch_flt = epoch + indbatch / self.per_epoch_batchs

            if indbatch % 10 == 0:
                log.info(
                    f"iter: {self.iter}, lr: {self.lr:g}, epoch: {epoch_flt:.2f}, loss: {loss.item():.2f}, hm_loss: {hm_loss.item():.2f}, "
                    f"box_loss: {reg_loss.item():.2f}, lmdk_loss: {landmark_loss.item():.5f}"
                )

            if indbatch % 1000 == 0:
                log.info("save hm")
                hm_image = hm[0, 0].cpu().data.numpy()
                common.imwrite(f"{jobdir}/imgs/hm_image.jpg", hm_image * 255)
                common.imwrite(f"{jobdir}/imgs/hm_image_gt.jpg", heatmap_gt[0, 0].cpu().data.numpy() * 255)

                image = np.clip((images[0].permute(1, 2, 0).cpu().data.numpy() * self.std + self.mean) * 255, 0, 255).astype(np.uint8)
                outobjs = eval_tool.detect_images_giou_with_netout(hm, tlrb, landmark, threshold=0.1, ibatch=0)

                im1 = image.copy()
                for obj in outobjs:
                    common.drawbbox(im1, obj)
                common.imwrite(f"{jobdir}/imgs/train_result.jpg", im1)



    def train(self):

        lr_scheduer = {
            1: 1e-3,
            2: 2e-3,
            3: 1e-3,
            60: 1e-4,
            120: 1e-5
        }

        # train
        self.model.train()
        for epoch in range(self.epochs):

            if epoch in lr_scheduer:
                self.set_lr(lr_scheduer[epoch])

            self.train_epoch(epoch)
            file = f"{jobdir}/models/{epoch + 1}.pth"
            common.mkdirs_from_file_path(file)
            torch.save(self.model.module.state_dict(), file)


trial_name = "small-H-dense-wide64-UCBA-keep12-noext-ignoresmall2"
jobdir = f"jobs/{trial_name}"

log = logger.create(trial_name, f"{jobdir}/logs/{trial_name}.log")
app = App("webface/train/label.txt", "webface/WIDER_train/images")
app.train()