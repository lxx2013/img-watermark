#coding=utf-8
from skimage import io,data,color
im = io.imread("gl1.jpg")
io.imshow(im),io.show()
im  = im.astype(np.float64) /255
mark = io.imread('watermark.jpg')
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
io.imshow(im_out),io.show()
