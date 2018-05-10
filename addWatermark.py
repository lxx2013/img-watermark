#coding=utf-8
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,imshow,show,title,subplot
import numpy as np

im=Image.open('gl1.jpg')
im = np.array(im)
im  = im.astype(np.float64) /255
mark = Image.open('watermark.jpg')
mark = np.array(mark)
mark = mark.astype(np.float64) /255

#symmetric
imsize = im.shape
mark_ = np.zeros([imsize[0],imsize[1],imsize[2]])
for i in range(mark.shape[0]):
    for j in range(mark.shape[1]):
        mark_[i,j,:] = mark[i,j,:]
        mark_[imsize[0]-1-i,imsize[1]-1-j,:]=mark[i,j,:]

#add watermark
im_fft = np.fft.fft2(im)
im_add = im_fft + mark_
im_out = np.fft.ifft2(im_add)
im_out = im_out.astype(np.float64)*255
im_out = im_out.astype(np.int32)
