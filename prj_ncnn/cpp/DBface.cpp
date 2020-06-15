//
// Created by chenjun on 2020/5/25.
//

#include "DBface.h"

DBface::DBface() {

}


DBface::~DBface() {
    net.clear();
}


int DBface::init(std::string param, std::string bin) {
    int param_ret = net.load_param(param.data());
    int bin_ret = net.load_model(bin.data());
    if (param_ret == 0 && bin_ret ==0)
        return 0;
    return 1;
}


void DBface::dynamic_resize(int src_h, int src_w, int stride) {
    d_h = (int)(ceil(src_h / stride) * stride);
    d_w = (int)(ceil(src_w / stride) * stride);

    scale_h = float(src_h) / d_h;
    scale_w = float(src_w) / d_w;
}


int DBface::pre_process(ncnn::Mat image, ncnn::Mat &out) {
    ncnn::Mat in = image;
    int src_h = image.h;
    int src_w = image.w;

    if (fixed_h && fixed_w)
    {
        fix_scale_h = float(src_h) / fixed_h;
        fix_scale_w = float(src_w) / fixed_w;
        ncnn::resize_bilinear(image, in, fixed_w, fixed_h);     // for fixed size inference
    }
    else if (src_h > max_image_size || src_w > max_image_size)  // for max image size limit
    {
        if (src_w > src_h)
        {
            fixed_w = max_image_size;
            fixed_h = (int)(src_h * max_image_size / src_w);
        } else
        {
            fixed_h = max_image_size;
            fixed_w = (int)(src_w * max_image_size / src_h);
        }

        fix_scale_h = float(src_h) / fixed_h;
        fix_scale_w = float(src_w) / fixed_w;
        ncnn::resize_bilinear(image, in, fixed_w, fixed_h);
    }

    int c, h, w;
    c = in.c;
    h = in.h;
    w = in.w;
    float *data = (float *)(in.data);

    for (int i = 0; i < c; ++i) {
        for (int j = 0; j < h; ++j) {
            for (int k = 0; k < w; ++k) {
                data[i*h*w + j*w + k] /= 255;
            }
        }
    }

    in.substract_mean_normalize(mean_value, std_value);

    image_h = in.h;
    image_w = in.w;
    dynamic_resize(image_h, image_w);               // for 32 scale

    ncnn::resize_bilinear(in, out, d_w, d_h);
}


void DBface::get_ids(float *data, int h, int w, float score, std::vector<std::pair<int, int>> &ids)
{
    if (data == NULL)
    {
        printf("[get_ids] wrong");
    }

    for (int i = 0; i < h ; ++i) {
        for (int j = 0; j < w ; ++j) {
            if (data[i*w + j] > score)
            {
                ids.push_back(std::make_pair(i, j));
            }
        }
    }
}


void DBface::nms(std::vector<FaceInfo> &input, std::vector<FaceInfo> &output, float nmsthreshold)
{
//    std::sort(input.begin(), input.end(), [](const FaceInfo a, const FaceInfo b)
//    {
//        return a.score > b.score;
//    });

    float iou = 0.f;
    float x1, y1, x2, y2;
    float w, h, intersection;
    std::vector<int> Picks;

    std::multimap<float, int > vscores;
    for (int i = 0; i < input.size() ; ++i) {
        vscores.insert(std::make_pair(input[i].score, i));
    }

    while (vscores.size() > 0){
        int first = vscores.rbegin()->second;       // multimap会自动对键升序排列
        Picks.push_back(first);

        for (std::multimap<float, int>::iterator it = vscores.begin(); it != vscores.end(); ) {
            int current_idx = it->second;
            x1 = std::max(input[current_idx].x1, input[first].x1);
            y1 = std::max(input[current_idx].y1, input[first].y1);
            x2 = std::min(input[current_idx].x2, input[first].x2);
            y2 = std::min(input[current_idx].y2, input[first].y2);

            w = ((x2 - x1 + 1) > 0) ? (x2 - x1 + 1) : 0;
            h = ((y2 - y1 + 1) > 0) ? (y2 - y1 + 1) : 0;
            intersection = w * h;

            if (nms_type == nms_union)
                iou = intersection / (input[current_idx].area + input[first].area - intersection);
            else if (nms_type == nms_min)
                iou  = intersection / std::min(input[current_idx].area, input[first].area);
            else
                std::cout << "[nms] | something wrong" << std::endl;

            if (iou > nmsthreshold) {
                it = vscores.erase(it);
            } else{
                it++;
            }
        }
    }

    output.resize(Picks.size());
    for (int j = 0; j < Picks.size(); ++j) {
        output[j] = input[Picks[j]];
    }

}


float DBface::Exp(float v)
{
    float gate = 1;
    if (abs(v) < gate)
        return v * exp(gate);

    if (v > 0)
        return exp(v);
    else
        return -exp(-v);
}

int DBface::decode(ncnn::Mat &pool_hm, ncnn::Mat &box, ncnn::Mat &landmark, std::vector<FaceInfo> &face,
                   float score_thresh)
{
    float *hm = (float*)(pool_hm.data);
    float *box_p = (float*)(box.data);
    float *landmark_p = (float*)(landmark.data);
    int hm_h = pool_hm.h;
    int hm_w = pool_hm.w;
    int spacial_size = hm_h * hm_w;
    int box_c = box.c;

    std::vector<std::pair<int, int>> ids;
    get_ids(hm, hm_h, hm_w, score_thresh, ids);

    std::vector<FaceInfo> face_temp;
    std::vector<std::pair<int, int>>::iterator read;

    int cx, cy;
    int index, index_lx, index_ly;
    float x1, x2, y1, y2, score, area;
    float lx, ly;

    for (read=ids.begin(); read != ids.end(); read++)
    {
        FaceInfo facebox;

        cy = (*read).first;
        cx = (*read).second;
        index = cy*hm_w + cx;
        x1 = box_p[0*spacial_size + index];
        y1 = box_p[1*spacial_size + index];
        x2 = box_p[2*spacial_size + index];
        y2 = box_p[3*spacial_size + index];
        score = hm[index];

        x1 = (cx - x1) * stride;
        y1 = (cy - y1) * stride;
        x2 = (cx + x2) * stride;
        y2 = (cy + y2) * stride;
        area = (x2 - x1) * (y2 - y1);

        facebox.x1 = x1; facebox.y1 = y1; facebox.x2 = x2; facebox.y2 = y2; facebox.area = area; facebox.score = score;

        for (int i = 0; i < 5; ++i) {
            index_lx = i * spacial_size + index;
            index_ly = (i + 5) * spacial_size + index;
            lx = Exp(landmark_p[index_lx] * stride);
            ly = Exp(landmark_p[index_ly] * stride);
            facebox.landmark[i * 2 + 0] = (lx + cx) * stride;
            facebox.landmark[i * 2 + 1] = (ly + cy) * stride;
        }
        face_temp.push_back(facebox);
    }

    nms(face_temp, face);

    for (int j = 0; j < face.size(); ++j) {
        face[j].x1 *= scale_w * fix_scale_w;
        face[j].x2 *= scale_w * fix_scale_w;
        face[j].y1 *= scale_h * fix_scale_h;
        face[j].y2 *= scale_h * fix_scale_h;
        for (int i = 0; i < 5; ++i) {
            face[j].landmark[i * 2 + 0] *= scale_w * fix_scale_w;
            face[j].landmark[i * 2 + 1] *= scale_h * fix_scale_h;
        }
    }

}


void DBface::squarebox(std::vector<FaceInfo> & face)
{
    float w, h, maxsize;
    float cx, cy;

    for (int i = 0; i < face.size(); ++i) {
        w = (face[i].x2 - face[i].x1);
        h = (face[i].y2 - face[i].y1);

        cx = face[i].x1 + w / 2;
        cy = face[i].y1 + h / 2;

        maxsize = w > h ? w : h;

        face[i].x1 = (cx - maxsize / 2 + 1) > 0 ? cx - maxsize / 2 + 1 : 0;
        face[i].y1 = (cy - maxsize / 2 + 1) > 0 ? cy - maxsize / 2 + 1 : 0;
        face[i].x2 = (cx + maxsize / 2 - 1) < image_w ? cx + maxsize / 2 -1 : image_w - 1;
        face[i].y2 = (cy + maxsize / 2 - 1) < image_h ? cy + maxsize / 2 -1 : image_h - 1;
    }
}


int DBface::detect(ncnn::Mat &image, std::vector<FaceInfo> & Face) {
    ncnn::Mat in;
    pre_process(image, in);

    ncnn::Extractor ex = net.create_extractor();
    ex.input("0", in);

    ncnn::Mat center, box, landmark;
    ex.extract("pool_hm", center);
    ex.extract("tlrb", box);
    ex.extract("landmark", landmark);

    decode(center, box, landmark, Face);
//    squarebox(Face);
    return 0;
}