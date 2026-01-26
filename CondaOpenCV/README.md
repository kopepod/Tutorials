# CondaOpenCV

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1khiOwLOBPNGTnqMOmTXQdqRbtEDkzTad)

This repository is meant to run opencv using the conda environment

## Conda

Create the envirorment. Alternatively a _yml_ file can be used.

```bash
conda create --name opencvenv
```

Activate the environment

```bash
conda activate opencvenv
```

## PIP

Install packages. 

```bash
pip install opencv-python
```

## Python

```python
#Demo.py
import cv2
import os

if not os.path.exists("church.jpg"):
  print("getting image ...")
  os.system("wget https://github.com/kopepod/Tutorials/blob/c02868ea337345d7386afecd9df531ca3474490d/CondaOpenCV/church.jpg")

img = cv2.imread('church.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
kp = sift.detect(gray, None)
img = cv2.drawKeypoints(gray, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite('output_church_sift_kp.jpg', img)

```

Desired output

```bash
python Demo.py
```
<img src="https://github.com/kopepod/Tutorials/blob/0c1a3bce84d22d9490d9ba75f895d5b96ae7f39f/CondaOpenCV/output_church_sift_kp.jpg" width="400" height="250" />


