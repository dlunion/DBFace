# WiderFace-Eval-Python
wider face验证集的测评代码  

一、生成预测结果  
生成以下预测结果：  
```python
 0--Parade
 0_Parade_marchingband_1_20.txt
 0_Parade_marchingband_1_74.txt
 ...
 1--Handshaking
```
其中，0--Parade是不同场景的文件夹，wider face总共有61种场景，0_Parade_marchingband_1_20.txt是对应某个图片的预测结果，其具有以下格式：  
```python
image_name
the number fo faces  #  检测出多少张人脸
x, y, w, h, confidence  #  x和y是检测框左上角的坐标
```
举个例子：  
```python
0_Parade_marchingband_1_309.jpg
536
499.62817 73.10439 34.215393 38.730423 0.93176836
47.55735 86.14974 21.215218 25.779213 0.7041396
```

二、下载ground truth数据  
可以从官网下载，得到这四个文件：`wider_easy_val.mat, wider_face_val.mat, wider_hard_val.mat, wider_medium_val.mat`  
官网下载可能有点慢，可以从这里下载：https://pan.baidu.com/s/1AErRlTlYaok6p7OGV7VShQ  

三、编译工具  
执行命令：  

    python3 setup.py build_ext --inplace

四、测AP  
```python
python3 evaluation.py -p <your prediction dir> -g <groud truth dir>  # 测easy,medium,hard的结果
```
```python
python3 evaluation.py -p <your prediction dir> -g <groud truth dir> --all # 将easy,medium,hard一起测
```

