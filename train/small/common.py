
import cv2
import random
import xml.etree.cElementTree as ET
import numpy as np
import math
import os

class BBox:

    def __init__(self, label, xyrb, score=0, landmark=None, rotate=False):
        self.label = label
        self.score = score
        self.landmark = landmark
        self.x, self.y, self.r, self.b = xyrb
        self.rotate = rotate
        
        minx = min(self.x, self.r)
        maxx = max(self.x, self.r)
        miny = min(self.y, self.b)
        maxy = max(self.y, self.b)
        self.x, self.y, self.r, self.b = minx, miny, maxx, maxy

    def __repr__(self):
        landmark_formated = ",".join([str(item[:2]) for item in self.landmark]) if self.landmark is not None else "empty"
        return f"(BBox[{self.label}]: x={self.x:.2f}, y={self.y:.2f}, r={self.r:.2f}, " + \
            f"b={self.b:.2f}, width={self.width:.2f}, height={self.height:.2f}, landmark={landmark_formated})"

    @property
    def width(self):
        return self.r - self.x + 1

    @property
    def height(self):
        return self.b - self.y + 1

    @property
    def area(self):
        return self.width * self.height

    @property
    def haslandmark(self):
        return self.landmark is not None

    # [[x, y], [x, y], [x, y], [x, y], [x, y]] to [x, x, x, x, x, y, y, y, y, y]
    @property
    def x5y5_cat_landmark(self):
        x, y = zip(*self.landmark)
        return x + y

    @property
    def box(self):
        return [self.x, self.y, self.r, self.b]

    @box.setter
    def box(self, newvalue):
        self.x, self.y, self.r, self.b = newvalue

    @property
    def xywh(self):
        return [self.x, self.y, self.width, self.height]

    @property
    def center(self):
        return [(self.x + self.r) * 0.5, (self.y + self.b) * 0.5]

    # return cx, cy, cx.diff, cy.diff
    def safe_scale_center_and_diff(self, scale, limit_x, limit_y):
        cx = clip_value((self.x + self.r) * 0.5 * scale, limit_x-1)
        cy = clip_value((self.y + self.b) * 0.5 * scale, limit_y-1)
        return [int(cx), int(cy), cx - int(cx), cy - int(cy)]

    def safe_scale_center(self, scale, limit_x, limit_y):
        cx = int(clip_value((self.x + self.r) * 0.5 * scale, limit_x-1))
        cy = int(clip_value((self.y + self.b) * 0.5 * scale, limit_y-1))
        return [cx, cy]

    def clip(self, width, height):
        self.x = clip_value(self.x, width - 1)
        self.y = clip_value(self.y, height - 1)
        self.r = clip_value(self.r, width - 1)
        self.b = clip_value(self.b, height - 1)
        return self

    def iou(self, other):
        return computeIOU(self.box, other.box)


def computeIOU(rec1, rec2):
    cx1, cy1, cx2, cy2 = rec1
    gx1, gy1, gx2, gy2 = rec2
    S_rec1 = (cx2 - cx1 + 1) * (cy2 - cy1 + 1)
    S_rec2 = (gx2 - gx1 + 1) * (gy2 - gy1 + 1)
    x1 = max(cx1, gx1)
    y1 = max(cy1, gy1)
    x2 = min(cx2, gx2)
    y2 = min(cy2, gy2)
 
    w = max(0, x2 - x1 + 1)
    h = max(0, y2 - y1 + 1)
    area = w * h
    iou = area / (S_rec1 + S_rec2 - area)
    return iou


def intv(*value):

    if len(value) == 1:
        # one param
        value = value[0]

    if isinstance(value, tuple):
        return tuple([int(item) for item in value])
    elif isinstance(value, list):
        return [int(item) for item in value]
    elif value is None:
        return 0
    else:
        return int(value)


def floatv(*value):

    if len(value) == 1:
        # one param
        value = value[0]

    if isinstance(value, tuple):
        return tuple([float(item) for item in value])
    elif isinstance(value, list):
        return [float(item) for item in value]
    elif value is None:
        return 0
    else:
        return float(value)


def clip_value(value, high, low=0):
    return max(min(value, high), low)


def randrf(low, high):
    return random.uniform(0, 1) * (high - low) + low


def mkdirs_from_file_path(path):

    try:
        path = path.replace("\\", "/")
        p0 = path.rfind('/')
        if p0 != -1:
            path = path[:p0]

            if not os.path.exists(path):
                os.makedirs(path)

    except Exception as e:
        print(e)


def imread(path):
    return cv2.imdecode(np.fromfile(path, dtype=np.uint8), 1)


def imwrite(path, image):
    path = path.replace("\\", "/")
    mkdirs_from_file_path(path)

    suffix = path[path.rfind("."):]
    ok, data = cv2.imencode(suffix, image)

    if ok:
        try:
            with open(path, "wb") as f:
                f.write(data)
            return True
        except Exception as e:
            print(e)
    return False


_annotation_alllabel = None
def set_annotation_all_label(label):
    global _annotation_alllabel
    _annotation_alllabel = label


def load_annotations(path):
    global _annotation_alllabel

    tree = None
    try:
        tree = ET.ElementTree(file=path)
    except:
        pass

    if tree is None:
        return []

    root = tree.getroot()
    obj_annotboxs = root.findall("object")
    objs = []

    for obj in obj_annotboxs:
        obj_label = obj.find('name').text
        obj_box = obj.find('bndbox')
        xmin = int(obj_box.find('xmin').text)
        ymin = int(obj_box.find('ymin').text)
        xmax = int(obj_box.find('xmax').text)
        ymax = int(obj_box.find('ymax').text)
        annotbox = [xmin, ymin, xmax, ymax]

        if _annotation_alllabel is not None:
            obj_label = _annotation_alllabel

        objs.append(BBox(obj_label, annotbox))
    return objs



class RandomColor(object):
    def __init__(self, num):
        self.class_mapper = {}
        self.build(num)
        

    def build(self, num):

        self.colors = []
        for i in range(num):
            c = (i / (num + 1) * 360, 0.9, 0.9)
            t = np.array(c, np.float32).reshape(1, 1, 3)
            t = (cv2.cvtColor(t, cv2.COLOR_HSV2BGR) * 255).astype(np.uint8).reshape(3)
            self.colors.append(intv(tuple(t)))
        
        seed = 0xFF01002
        length = len(self.colors)
        for i in range(length):
            a = i
            seed = (((i << 3 ) + 3512301) ^ seed) & 0x0FFFFFFF
            b = seed % length
            x = self.colors[a]
            y = self.colors[b]
            self.colors[a] = y
            self.colors[b] = x

    def get_index(self, label):
        if isinstance(label, int):
            return label % len(self.colors)
        elif isinstance(label, str):
            if label not in self.class_mapper:
                self.class_mapper[label] = len(self.class_mapper)
            return self.class_mapper[label]
        else:
            raise Exception("label is not support type{}, must be str or int".format(type(label)))

    def __getitem__(self, label):
        return self.colors[self.get_index(label)]


_rand_color = None
def randcolor(label, num=32):
    global _rand_color

    if _rand_color is None:
        _rand_color = RandomColor(num)
    return _rand_color[label]



#(239, 121, 162)
def drawbbox(image, bbox, color=None, thickness=2, textcolor=(0, 0, 0), landmarkcolor=(0, 0, 255)):

    if color is None:
        color = randcolor(bbox.label)

    #text = f"{bbox.label} {bbox.score:.2f}"
    text = f"{bbox.score:.2f}"
    x, y, r, b = intv(bbox.box)
    w = r - x + 1
    h = b - y + 1

    cv2.rectangle(image, (x, y, r-x+1, b-y+1), color, thickness, 16)

    border = thickness / 2
    pos = (x + 3, y - 5)
    #cv2.rectangle(image, intv(x - border, y - 21, w + thickness, 21), color, -1, 16)
    #cv2.putText(image, text, pos, 0, 0.5, textcolor, 1, 16)

    if bbox.haslandmark:
        for i in range(len(bbox.landmark)):
            x, y = bbox.landmark[i][:2]
            cv2.circle(image, intv(x, y), 3, landmarkcolor, -1, 16)
            #cv2.putText(image, "%d" % i, intv(x, y-3), 0, 0.5, textcolor, 1, 16)


def find_files_fmt_xml(directory, suffix=".jpg"):

    files = []
    for d, ds, fs in os.walk(directory):
        files.extend([f"{d}/{file}" for file in fs if file.endswith(suffix)])

    imglist = files
    xmllist = [file[:file.rfind(".")] + ".xml" for file in files]
    return imglist, xmllist


def find_files(directory, suffix=".jpg"):

    files = []
    for d, ds, fs in os.walk(directory):
        files.extend([f"{d}/{file}" for file in fs if file.endswith(suffix)])
    return files


def gaussian_truncate_2d(shape, sigma_x=1, sigma_y=1):
    m, n = [(ss - 1.) / 2. for ss in shape]
    y, x = np.ogrid[-m:m + 1, -n:n + 1]

    h = np.exp(-(x * x / (2 * sigma_x * sigma_x) + y * y / (2 * sigma_y * sigma_y)))
    h[h < np.finfo(h.dtype).eps * h.max()] = 0
    return h


def draw_truncate_gaussian(heatmap, center, h_radius, w_radius, k=1):
    h_radius = math.ceil(h_radius)
    w_radius = math.ceil(w_radius)
    h, w = 2 * h_radius + 1, 2 * w_radius + 1
    sigma_x = w / 6
    sigma_y = h / 6
    gaussian = gaussian_truncate_2d((h, w), sigma_x=sigma_x, sigma_y=sigma_y)
    x, y = int(center[0]), int(center[1])

    height, width = heatmap.shape[0:2]

    left, right = min(x, w_radius), min(width - x, w_radius + 1)
    top, bottom = min(y, h_radius), min(height - y, h_radius + 1)

    masked_heatmap = heatmap[y - top:y + bottom, x - left:x + right]
    masked_gaussian = gaussian[h_radius - top:h_radius + bottom, w_radius - left:w_radius + right]
    if min(masked_gaussian.shape) > 0 and min(masked_heatmap.shape) > 0:
        np.maximum(masked_heatmap, masked_gaussian * k, out=masked_heatmap)
    return gaussian


def truncate_radius(sizes, stride=4):
    return [s / (stride * 4.0) for s in sizes]


def gaussian_2d(shape, sigma=1):
    m, n = [(ss - 1.) / 2. for ss in shape]
    y, x = np.ogrid[-m:m + 1, -n:n + 1]

    h = np.exp(-(x * x + y * y) / (2 * sigma * sigma))
    h[h < np.finfo(h.dtype).eps * h.max()] = 0
    return h



def draw_gaussian(heatmap, center, radius, k=1):
    diameter = 2 * radius + 1
    gaussian = gaussian_2d((diameter, diameter), sigma=diameter / 6)

    x, y = int(center[0]), int(center[1])

    height, width = heatmap.shape[0:2]

    left, right = min(x, radius), min(width - x, radius + 1)
    top, bottom = min(y, radius), min(height - y, radius + 1)

    masked_heatmap = heatmap[y - top:y + bottom, x - left:x + right]
    masked_gaussian = gaussian[radius - top:radius + bottom, radius - left:radius + right]
    if min(masked_gaussian.shape) > 0 and min(masked_heatmap.shape) > 0:  # TODO debug
        np.maximum(masked_heatmap, masked_gaussian * k, out=masked_heatmap)
    return heatmap


def gaussian_radius(det_size, min_overlap=0.7):
    height, width = math.ceil(det_size[0]), math.ceil(det_size[1])

    a1 = 1
    b1 = (height + width)
    c1 = width * height * (1 - min_overlap) / (1 + min_overlap)
    sq1 = np.sqrt(b1 ** 2 - 4 * a1 * c1)
    r1 = (b1 - sq1) / (2 * a1)

    a2 = 4
    b2 = 2 * (height + width)
    c2 = (1 - min_overlap) * width * height
    sq2 = np.sqrt(b2 ** 2 - 4 * a2 * c2)
    r2 = (b2 - sq2) / (2 * a2)

    a3 = 4 * min_overlap
    b3 = -2 * min_overlap * (height + width)
    c3 = (min_overlap - 1) * width * height
    sq3 = np.sqrt(b3 ** 2 - 4 * a3 * c3)
    r3 = (b3 + sq3) / (2 * a3)
    return min(r1, r2, r3)


def file_name_no_suffix(path):
    path = path.replace("\\", "/")

    p0 = path.rfind("/") + 1
    p1 = path.rfind(".")

    if p1 == -1:
        p1 = len(path)
    return path[p0:p1]


def file_name(path):
    path = path.replace("\\", "/")
    p0 = path.rfind("/") + 1
    return path[p0:]


def label2index_to_index2label(label2index_dic):

    index2label = {}
    for label in label2index_dic:
        index = label2index_dic[label]
        index2label[index] = label
    return index2label



def parse_facials_webface(facials):

    ts = []
    for facial in facials:
        x, y, w, h = facial[:4]
        box = [x, y, x + w - 1, y + h - 1]
        landmarks = None

        if w * h < 4 * 4:
            continue

        if len(facial) >= 19:
            landmarks = []
            for i in range(5):
                x, y, t = facial[i * 3 + 4:i * 3 + 4 + 3]
                if t == -1:
                    landmarks = None
                    break

                landmarks.append([x, y])

        ts.append(BBox(label="facial", xyrb=box, landmark=landmarks, rotate = False))
    return ts


def load_webface(labelfile, imagesdir):
    with open(labelfile, "r") as f:
        lines = f.readlines()
        lines = [line.replace("\n", "") for line in lines]

    stage = 0
    facials = []
    file = None
    files = []
    for index, line in enumerate(lines):
        if line.startswith("#"):
            if file is not None:
                files.append([f"{imagesdir}/{file}", parse_facials_webface(facials)])

            file = line[2:]
            facials = []
        else:
            facials.append([float(item) for item in line.split(" ")])

    if file is not None:
        files.append([f"{imagesdir}/{file}", parse_facials_webface(facials)])
    return files


def pad(image, stride=32):

    hasChange = False
    stdw = image.shape[1]
    if stdw % stride != 0:
        stdw += stride - (stdw % stride)
        hasChange = True 

    stdh = image.shape[0]
    if stdh % stride != 0:
        stdh += stride - (stdh % stride)
        hasChange = True

    if hasChange:
        newImage = np.zeros((stdh, stdw, 3), np.uint8)
        newImage[:image.shape[0], :image.shape[1], :] = image
        return newImage
    else:
        return image


def log(v):

    if isinstance(v, tuple) or isinstance(v, list):
        return [log(item) for item in v]

    elif isinstance(v, np.ndarray):
        return np.array([log(item) for item in v])
    
    base = np.exp(1)
    if abs(v) < base:
        return v / base
    
    if v > 0:
        return np.log(v)
    else:
        return -np.log(-v)
    

def exp(v):

    if isinstance(v, tuple) or isinstance(v, list):
        return [exp(item) for item in v]

    elif isinstance(v, np.ndarray):
        return np.array([exp(item) for item in v])
    
    gate = 1
    if abs(v) < gate:
        return v * np.exp(gate)
    
    if v > 0:
        return np.exp(v)
    else:
        return -np.exp(-v)