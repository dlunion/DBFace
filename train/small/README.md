### Quick Start

1. Download `WiderFace` dataset and `RetinaFace` landmark file.

   file tree:

   ```json
   webface:
   	train
   		label.txt
   	WIDER_train
   		images
   			0-Parade
   			...
   	val
   		label.txt
   	WIDER_val
   		images
   			0--Parade
   			...
   ```

2. Run `python train-small-H.py`



### MAP on WiderFace Val Dataset

| Method                 | Version | Size   | Easy  | Medium | Hard  |
| ---------------------- | ------- | ------ | ----- | ------ | ----- |
| RetinaFace-MobileNetV2 | Small   | 1.68MB | 0.896 | 0.871  | 0.681 |
| DBFace-Small-H(Ours)   | Small   | 1.75MB | 0.886 | 0.860  | 0.731 |



### Model

[download](http://zifuture.com:1000/fs/public_models/small.dense.wide64.ucba-467314bf.pth)