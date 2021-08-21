import cv2
# 在Opencv中的话，这个功能将会非常简单，图像的打开可以通过cv2.imread代码打开，cv2.cvtColor可以将图片转化为灰度图
# RGB 打开一张黑图片
img = cv2.imread('519194336.jpg')
# 将RGB图转化为灰度图。
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 你也可以在读取图片的时候增加一个额外的参数使得图像直接转化为灰度图
img_gray = cv2.imread('519194336.jpg', cv2.IMREAD_GRAYSCALE)
# 这里调用cv2.imread函数时，设置了cv2.IMREAD_GRAYSCALE的标志，表示加载灰度图。在imread函数中是设置了三种标志，分别是
#
#     cv2.IMREAD_COLOR : 默认使用该种标识。加载一张彩色图片，忽视它的透明度。
#
#     cv2.IMREAD_GRAYSCALE : 加载一张灰度图。
#
#     cv2.IMREAD_UNCHANGED : 加载图像，包括它的Alpha 通道(Alpha 表示图片的透明度)。
#
# 另外，如果觉得以上标志太长，可以简单使用 1，0，-1 代替，效果是相同的。
# 灰度图进行反色操作。
# 灰度图反色图像可以通过将灰度图每个像素点取反得到，由于灰度图的像素点的在0-255之间，将其取反的话就是255-当前像素点。
img_gray_inv = 255 - img_gray
# 对步骤2中的图片进行高斯模糊Gaussian
# blur。
# 将步骤1中的灰度图像和步骤三中的模糊反色图像混合，这里就用到亮化(Dodging)
# 和暗化(burning)
# 的技术。
cv2.imshow('original.jpg', gray)
cv2.waitKey(0)
# cv2.imwrite('original.jpg', gray)

