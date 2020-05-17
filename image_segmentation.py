# -*- coding: utf-8 -*-
"""Image_Segmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/184npTcKA8dGRlcuYZZ6W58KassuNrgWe
"""

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

import numpy as np
import matplotlib.pyplot as plt
import cv2
get_ipython().run_line_magic('matplotlib', 'inline')

image = cv2.imread('1_NPWZVvTqyEBQr8rBmsbm2g.jpeg')
plt.figure(figsize=(20,10))
plt.imshow(image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(20,10))
plt.imshow(image)

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.figure(figsize=(20,10))
plt.imshow(gray)

lower = 160
upper = 270

edges = cv2.Canny(gray, lower, upper)

plt.figure(figsize=(20,10))
plt.imshow(edges, cmap='gray')

pixel_vals = image.reshape((-1,3))
pixel_vals = np.float32(pixel_vals)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.2)
k = 7
retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.cv2.KMEANS_PP_CENTERS)
centers = np.uint8(centers)
segmented_data = centers[labels.flatten()]
segmented_image = segmented_data.reshape((image.shape))
labels_reshape = labels.reshape(image.shape[0], image.shape[1])
plt.figure(figsize=(20,10))
plt.imshow(segmented_image)

plt.figure(figsize=(20,10))
plt.imshow(labels_reshape==0, cmap='gray')

cluster = 0 
masked_image = np.copy(image)
masked_image[labels_reshape == cluster] = [0, 255, 0]
plt.figure(figsize=(20,10))
plt.imshow(masked_image)

cluster = 1
masked_image = np.copy(image)
masked_image[labels_reshape == cluster] = [128, 0, 128]
plt.figure(figsize=(20,10))
plt.imshow(masked_image)

cluster = 2
masked_image = np.copy(image)
masked_image[labels_reshape == cluster] = [0, 0, 255]
plt.figure(figsize=(20,10))
plt.imshow(masked_image)

cluster = 3
masked_image = np.copy(image)
masked_image[labels_reshape == cluster] = [0, 0, 255]
plt.figure(figsize=(20,10))
plt.imshow(masked_image)

cluster = 4
masked_image = np.copy(image)
masked_image[labels_reshape == cluster] = [128, 0, 128]
plt.figure(figsize=(20,10))
plt.imshow(masked_image)

cluster = 5
masked_image = np.copy(image)
masked_image[labels_reshape == cluster] = [128, 0, 128]
plt.figure(figsize=(20,10))
plt.imshow(masked_image)

