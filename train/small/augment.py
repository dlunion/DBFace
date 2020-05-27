
import random
import cv2
import numpy as np
from common import *



def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def lighting_(image, alphastd, eigval, eigvec):

    alpha = np.random.RandomState().normal(scale=alphastd, size=(3, ))
    image += np.dot(eigvec, eigval * alpha)

def blend_(alpha, image1, image2):
    image1 *= alpha
    image2 *= (1 - alpha)
    image1 += image2

def saturation_(image, gs, gs_mean, var):
    alpha = 1. + np.random.RandomState().uniform(low=-var, high=var)
    blend_(alpha, image, gs[:, :, None])

def brightness_(image, gs, gs_mean, var):
    alpha = 1. + np.random.RandomState().uniform(low=-var, high=var)
    image *= alpha

def contrast_( image, gs, gs_mean, var):
    alpha = 1. + np.random.RandomState().uniform(low=-var, high=var)
    blend_(alpha, image, gs_mean)

def augmentWithColorJittering(image, objs):
    eig_val = np.array([0.2141788, 0.01817699, 0.00341571],
                       dtype=np.float32)
    eig_vec = np.array([
        [-0.58752847, -0.69563484, 0.41340352],
        [-0.5832747, 0.00994535, -0.81221408],
        [-0.56089297, 0.71832671, 0.41158938]
    ], dtype=np.float32)
    functions = [brightness_, contrast_, saturation_]
    random.shuffle(functions)
    image = (image.astype(np.float32) / 255.)
    gs = grayscale(image)
    gs_mean = gs.mean()
    for f in functions:
        f(image, gs, gs_mean, 0.3)
    lighting_(image, 0.1, eig_val, eig_vec)
    image = image *255.
    image = np.uint8(np.clip(image, 0, 255))
    return image, objs

def limitbox(box, width, height):
    x, y, r, b = box
    x = int(clip_value(x, width - 1))
    y = int(clip_value(y, height - 1))
    r = int(clip_value(r, width - 1))
    b = int(clip_value(b, height - 1))
    return [x, y, r, b]

def bounding(objs, width, height):
    x, y, r, b = [width - 1, height - 1, 0, 0]
    if len(objs) == 0:
        w, h = [width * randrf(0.3, 0.8), height * randrf(0.3, 0.8)]
        x = randrf(0, 1) * (width - w)
        y = randrf(0, 1) * (height - h)
        r = x + w - 1
        b = y + h - 1
    else:
        for obj in objs:
            x = min(x, obj.x)
            y = min(y, obj.y)
            r = max(r, obj.r)
            b = max(b, obj.b)
    return limitbox([x, y, r, b], width, height)


def transObjs(matrix, objs, scale):
    points = np.ones((3, len(objs ) * 6 ), np.float32)
    for index, obj in enumerate(objs):
        x, y, r, b = obj.box
        center_x =  (x + r)/2.
        center_y =  (y + b)/2
        points[:2, index * 6 + 0] = center_x, center_y

        if obj.haslandmark:
            for i in range(len(obj.landmark)):
                points[:2, index * 6 + 1 + i] = obj.landmark[i]

    points = np.matmul(matrix, points)
    newobjs = []
    for index, obj in enumerate(objs):
        center_x, center_y = points[:2, index * 6 + 0]
        box_x, box_y, box_r, box_b = obj.box
        width  =  (box_r - box_x)*scale
        height =  (box_b - box_y)*scale
        x = center_x - 0.5 * width
        y = center_y - 0.5 * height
        r = center_x + 0.5 * width
        b = center_y + 0.5 * height
        landmark = None

        if obj.haslandmark:
            landmark = []
            for i in range(len(obj.landmark)):
                landmark.append(points[:2, index * 6 + 1 + i])

        newobjs.append(BBox(label=obj.label, xyrb=[x, y, r, b], landmark=landmark, rotate= obj.rotate))
    return newobjs


def augmentWithFlip(img, objs):
    img_dst = cv2.flip(img, 1)
    image_width = img_dst.shape[1]

    for obj in objs:
        dst_x = image_width - obj.r
        dst_r = image_width - obj.x
        obj.x = dst_x
        obj.r = dst_r

        if obj.haslandmark:
            for i in range(len(obj.landmark)):
                obj.landmark[i][0] = image_width - obj.landmark[i][0]

            p0, p1, p2, p3, p4 = obj.landmark
            obj.landmark = [p1, p0, p2, p4, p3]

    return img_dst, objs


def computeIoUMin(rec1, rec2):
    cx1 ,cy1 ,cx2 ,cy2 =rec1
    gx1 ,gy1 ,gx2 ,gy2 =rec2
    # 计算每个矩形的面积
    S_rec1 = (cx2 - cx1) * (cy2 - cy1)  # C的面积
    S_rec2 = (gx2 - gx1) * (gy2 - gy1)  # G的面积

    # 计算相交矩形
    x1 = max(cx1, gx1)
    y1 = max(cy1, gy1)
    x2 = min(cx2, gx2)
    y2 = min(cy2, gy2)

    w = max(0, x2 - x1)
    h = max(0, y2 - y1)
    area = w * h  # C∩G的面积
    iou = area / min(S_rec1, S_rec2)
    return iou


def cubeTransform(image, objs, outw, outh, keepsize=8):
    max_wh = max(image.shape[0], image.shape[1])
    newImage = np.zeros((max_wh, max_wh, 3), np.uint8)
    newImage[:image.shape[0], :image.shape[1], :] = image
    newImage = cv2.resize(newImage, (outw, outh) )
    scalar_x = max_wh/outw
    scalar_y = max_wh/outh

    for obj in objs:
        obj.x /= scalar_x
        obj.y /= scalar_y
        obj.r /= scalar_x
        obj.b /= scalar_y
        if obj.haslandmark:
            for lm in obj.landmark:
                lm[0] /= scalar_x
                lm[1] /= scalar_y

    for i in range(len(objs) - 1, -1, -1):
        if objs[i].area < keepsize * keepsize:
            del objs[i]

    return newImage, objs


def augmentWithCropScaleWebface(image, objs, outw=800, outh=800, mode='normal', keepsize=8):

    oldobjs = objs
    width, height = image.shape[1], image.shape[0]
    scale = 1.
    angle = 0.
    cx = 0.5 * width
    cy = 0.5 * height

    if mode == "normal":
        scale = randrf(0.5, 2.0)
        if randrf(0, 1) > 0.8:
            scale = 1	

        cx = randrf(0.1, 0.9) * width
        cy = randrf(0.1, 0.9) * height
		
        if randrf(0, 1) > 0.5:
            angle = randrf(-45, 45)

    elif mode == "cube":
        if randrf(0, 1) > 0.5:
            angle = randrf(-45, 45)
            scale = randrf(0.9, 1.2)
            cx = randrf(0.4, 0.6) * width
            cy = randrf(0.4, 0.6) * height

    M = cv2.getRotationMatrix2D((cx, cy), angle, scale)
    M[0, 2] -= cx - outw * 0.5
    M[1, 2] -= cy - outh * 0.5
    objs = transObjs(M, objs, scale)

    boximage = [0, 0, outw - 1, outh - 1]
    for i in range(len(objs) - 1, -1, -1):
        ioumin = computeIoUMin(objs[i].box, boximage)
        if ioumin < 0.10 or objs[i].area < keepsize * keepsize:
            del objs[i]

    if len(objs) == 0 and randrf(0, 1) > 0.5:
        return augmentWithCropScaleWebface(image, oldobjs, outw, outh, mode)

    image = cv2.warpAffine(image, M, (outw, outh))
    if abs(angle) >30:
        for obj in objs:
            obj.rotate = True
    return image, objs


def webface(image, objs, outw=800, outh=800, keepsize=8):

    funcs = [[augmentWithColorJittering, 0.7], [augmentWithFlip, 0.7]]
    random.shuffle(funcs)
    num = len(funcs)
    for n in range(num):
        func, freq = funcs[n]
        if randrf(0, 1) < freq:
            image, objs = func(image, objs)

    if randrf(0, 1) > 0.5:
        image, objs = cubeTransform(image, objs,  outw, outh, keepsize=keepsize)
        image, objs = augmentWithCropScaleWebface(image, objs, outw, outh, 'cube', keepsize=keepsize)
    else:
        image, objs = augmentWithCropScaleWebface(image, objs, outw, outh, keepsize=keepsize)

    return image, objs