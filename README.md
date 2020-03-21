# DBFace
DBFace is a single-stage face detector 



## MAP@0.5 Result on val set of WiderFace

*  Single Scale Inference on the Original Image

Method | Version | Size | Easy | Medium | Hard
-|-|-|-|-|-
RetinaFace-MobileNetV2 | Small | 1.68MB  | 0.896 | 0.871 | 0.681
DBFace-MobileNetV3-ReLU | Large | 7.4MB | 0.883 | **0.880** | **0.786** 
CenterFace-MobileNetV2 | Large | 7.3MB | ? | ? | ?



## Result on DBFace (threshold = 0.2)

![selfie](result/selfie.draw.jpg)

---

## Result on RetinaFace-MobileNetV2 (threshold=0.2)

* [link.retinaface](https://github.com/deepinsight/insightface/tree/master/RetinaFace)

![retinaface](result/selfie.retinaface.draw.jpg)



## Result on CenterFace-MobileNetV2 (threshold=?)

* [link.centerface](https://github.com/Star-Clouds/CenterFace)

![selfie.centerface.draw.jpg](result/selfie.centerface.draw.jpg)



## References

1. Hamid Rezatofighi1, Generalized Intersection over Union: A Metric and A Loss for Bounding Box Regression：https://arxiv.org/abs/1902.09630

2. Xingyi Zhou, Objects as Points：https://arxiv.org/abs/1904.07850

3. Zili Liu, Training-Time-Friendly Network for Real-Time Object Detection：https://arxiv.org/abs/1909.00700

4. Zhen-Hua Feng, Wing Loss for Robust Facial Landmark Localisation with Convolutional Neural Networks: https://arxiv.org/abs/1711.06753v4

5. Mahyar Najib, SSH: Single Stage Headless Face Detector: https://arxiv.org/abs/1708.03979
