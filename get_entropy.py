# coding: utf-8
#python检测“无内容”图片
#通过图像熵检测，无内容图像熵较小，可通过设置阈值检测无内容图像
import cv2
import numpy as np
import math
import time
import os
import shutil
def get_entropy(img_):
    x, y = img_.shape[0:2]
    img_ = cv2.resize(img_, (100, 100)) # 缩小的目的是加快计算速度
    tmp = []
    for i in range(256):
        tmp.append(0)
    val = 0
    k = 0
    res = 0
    img = np.array(img_)

    for i in range(len(img)):
        for j in range(len(img[i])):
            val = img[i][j]

            tmp[val] = float(tmp[val] + 1)
            k =  float(k + 1)
    for i in range(len(tmp)):
        tmp[i] = float(tmp[i] / k)
    for i in range(len(tmp)):
        if(tmp[i] == 0):
            res = res
        else:
            res = float(res - tmp[i] * (math.log(tmp[i]) / math.log(2.0)))
    return res
if __name__ == '__main__':

    original = cv2.imread('C:\\Users\\40520\Pictures\\5-steps.png',0)
    res = get_entropy(original)
    print(res)


