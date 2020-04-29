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

2. Run `python train-small-H-keep12-noext-ignoresmall2.py`



### MAP on WiderFace Val Dataset

| Method                     | Version | Size       | Easy  | Medium | Hard      |
| -------------------------- | ------- | ---------- | ----- | ------ | --------- |
| RetinaFace-MobileNetV2     | Small   | 1.68MB     | 0.896 | 0.871  | 0.681     |
| DBFace-Small-H-NoExt(Ours) | Small   | **1.30MB** | 0.895 | 0.870  | **0.713** |
| DBFace-Small-H(Ours)       | Small   | **1.73MB** | **0.899** | **0.876** | **0.728** |
