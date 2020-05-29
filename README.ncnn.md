## 1. 效果
先上效果，密集。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200527184001865.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE2MjIyMDg=,size_16,color_FFFFFF,t_70)

## 2.特点
- 完全依赖原[DBface](https://github.com/dlunion/DBFace)项目的模型
- 输出的ncnn模型支持bilinear2d上采样
- 模型超小（1.3M）
- 和pytorch框检相同的输出
- android手机上简单性能测试
- class封装，方便调用

## 3. requirements
- opencv(安装opencv，并配置，让cmake能找到)


## 4. 使用
1. 按如下修改CMakeList.txt
```bash
# 设置变量
set (DIR /ncnn/ncnn-20180704/build/install)         # 修改`/ncnn/ncnn-20180704/build/install`为自己ncnn对应的位置
```

2. 编译
```bash
cd $project/prj_ncnn
mkdir build && cd build
cmake ..
make

# 测试
./demo ../model/model527.param ../model/model527.bin ../model/test.jpg
```

5. 在android上的简单性能测试

| 处理器 |  RAM  |  图像尺寸      |     时间(ms)   |     是否使用GPU   |
|:--------:| :-------------:|:--------:|:--------:|:--------:|
| 骁龙710 |    6G   | 640*480 |  497 |    否    |
| 骁龙855 |   12G  | 640*480 | 238  |     否   |




