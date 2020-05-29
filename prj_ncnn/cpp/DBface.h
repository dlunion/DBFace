//
// Created by chenjun on 2020/5/25.
//

#ifndef DEMO_TEST_H
#define DEMO_TEST_H

#include <opencv2/opencv.hpp>
#include <mat.h>
#include <net.h>
#include <string>
#include <vector>
#include <math.h>

enum NMS_TYPE{nms_union, nms_min};

typedef struct FaceInfo{
    float x1;
    float y1;
    float x2;
    float y2;
    float score;
    float area;
    float landmark[10];
} Facestruct;

class DBface{

    ncnn::Net net;

    const float mean_value[3] = {0.408f, 0.447f, 0.47f};
    const float std_value[3] = {1/0.289f, 1/0.274f, 1/0.278f};
    int fixed_h = 2220;            // for fixed size inference
    int fixed_w = 3072;
    float fix_scale_h = 1.f;
    float fix_scale_w = 1.f;
    const int max_image_size = 1024;


    const int stride = 4;
    NMS_TYPE nms_type = nms_union;

    int d_h, d_w;
    float scale_h, scale_w;
    int image_h, image_w;

public:
    int init(std::string param, std::string bin);
    int detect(ncnn::Mat &image, std::vector<FaceInfo> & face);

    DBface();
    ~DBface();

private:
    int pre_process(ncnn::Mat image, ncnn::Mat &output);
    void dynamic_resize(int src_h, int src_w, int stride=32);
    void get_ids(float *data, int h, int w, float score, std::vector<std::pair<int, int>> & ids);
    void nms(std::vector<FaceInfo> & input, std::vector<FaceInfo> & output, float nmsthreshold=0.2);
    int decode(ncnn::Mat & pool_hm, ncnn::Mat & box, ncnn::Mat & landmark, std::vector<FaceInfo> & face, float score_thresh=0.5);
    void squarebox(std::vector<FaceInfo> & face);
    float Exp(float x);

};

#endif //DEMO_TEST_H
