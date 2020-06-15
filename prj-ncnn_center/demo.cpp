#include <iostream>
#include <opencv2/opencv.hpp>
#include "ncnn_centerface.h"

int main(int argc, char** argv) {
//	if (argc !=3)
//	{
//		std::cout << " .exe mode_path image_file" << std::endl;
//		return -1;
//	}

	std::string model_path = "./model";
	std::string image_file = "./model/selfie.jpg";

	Centerface centerface;


	centerface.init(model_path);

	cv::Mat image = cv::imread(image_file);
    ncnn::Mat inmat = ncnn::Mat::from_pixels(image.data, ncnn::Mat::PIXEL_BGR2RGB, image.cols, image.rows);

	std::vector<FaceInfo> face_info;
	centerface.detect(inmat, face_info, image.cols, image.rows);

	for (int i = 0; i < face_info.size(); i++) {
		cv::rectangle(image, cv::Point(face_info[i].x1, face_info[i].y1), cv::Point(face_info[i].x2, face_info[i].y2), cv::Scalar(0, 255, 0), 2);
		for (int j = 0; j < 5; j++) {
			cv::circle(image, cv::Point(face_info[i].landmarks[2*j], face_info[i].landmarks[2*j+1]), 2, cv::Scalar(255, 255, 0), 2);
		}
	}

	cv::imshow("test", image);
	cv::waitKey(0);

	return 0;
}