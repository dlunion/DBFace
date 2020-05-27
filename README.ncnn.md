## 1. 效果
先上效果，密集。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200527184001865.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE2MjIyMDg=,size_16,color_FFFFFF,t_70)

## 2.路线
- pytorch2onnx
- 解决bilinear2d上采样问题
- 编译ncnn
- 创建项目，导入libncnn，完善DBface的推理代码
- 解决nms有重框的问题

## 3. 具体事项
1. 图像预处理：((image / 255 - mean) / std).astype(np.float32)
项目初始调试成功的时候，结果和DBface.pytorch推理的结果有很大差距。从以下几个方面进行了检验。
- 后面对导出的onnx模型进行了检验
- 对onnx2ncnn的导出进行了检查
- 检查ncnn项目的数据预处理
  +  最后发现是数据预处理部分的问题。问题出在`in.substract_mean_normalize`，其中的源码是 `× norm_value`，所以需要对DBface的std_value取倒
  + 其次是`image/255`这部分，最初是`cv::Mat image/255`发现还是有问题，后面是先cv::Mat > ncnn::Mat，然后再 / 255.
  + 
对应的ncnn项目代码：
```cpp
// 1. DBface的std取倒数
const float mean_value[3] = {0.408f, 0.447f, 0.47f};
const float std_value[3] = {1/0.289f, 1/0.274f, 1/0.278f};

// 2.先转到ncnn::Mat,再/255
in = ncnn::Mat::from_pixels(image.data, ncnn::Mat::PIXEL_BGR, image.cols, image.rows);

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
```

## TO DO
- [ ] 移植到android
- [ ] 使android项目支持GPU
- [ ] 速度测试报告
