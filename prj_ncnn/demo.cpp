//
// Created by chenjun on 2020/5/25.
//
#include "DBface.h"

int main(int argc, char** argv){
//    std::string model_param = "./model/model527.param";
//    std::string model_bin = "./model/model527.bin";
//    std::string test_image = "./model/selfie.jpg";

    std::string model_param, model_bin, test_image;
    if (argc != 4){
        printf("please set the param/bin/jpg path");
        return -1;
    }
    model_param = argv[1];
    model_bin = argv[2];
    test_image = argv[3];

    DBface dbface;

    dbface.init(model_param, model_bin);

    ncnn::Mat in_mat;
    cv::Mat image = cv::imread(test_image);

    in_mat = ncnn::Mat::from_pixels(image.data, ncnn::Mat::PIXEL_BGR, image.cols, image.rows);

    // inference
    std::vector<FaceInfo> Facebox;
    int ret = dbface.detect(in_mat, Facebox);

    printf("detect face nums:%d \n", (int)Facebox.size());

    // show detect results
    for (int i = 0; i < Facebox.size(); ++i) {
        cv::rectangle(image, cv::Point(Facebox[i].x1, Facebox[i].y1), cv::Point(Facebox[i].x2, Facebox[i].y2), cv::Scalar(0,0,255), 2);
        for (int j = 0; j < 5; ++j) {
            cv::circle(image, cv::Point(Facebox[i].landmark[j*2+0], Facebox[i].landmark[j*2+1]), 2, cv::Scalar(255,255,0), 2);
        }
    }

    cv::imshow("DBface", image);
    cv::waitKey(0);

    return 0;
}
