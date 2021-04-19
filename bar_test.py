import cv2 as cv
resized1 = cv.imread('temp0.jpg')#读取最开始读入的图片
#cv.imshow('resized1-0.jpg', resized1)
#cv.waitKey(10)
img = cv.imread('output.jpg')#读取生成的烟雾图

resized0 = cv.resize(img, (weight, height), interpolation=cv.INTER_AREA)
#cv.imshow('resized0.jpg', resized0)
#cv.waitKey(10)

#嵌入图片，resized1是原图，resized0是烟雾图片，中括号内为嵌入的坐标
resized1[global_y0:height+global_y0, global_x0:weight+global_x0] = resized0
#cv.imshow('resized1.jpg', resized1)
cv.imwrite('temp1.jpg', resized1)
resized2 = resized1  # 将最终生成的图片复制到全局变量中，在保存按钮中进行保存
#cv.imwrite('resized2.jpg', resized2)
global final_picture # 此处声明该图片为全局变量
final_picture=resized2 #将最终生成的图片复制到全局变量中，在保存按钮中进行保存
#cv.imwrite('final_picture0.jpg', final_picture)
#cv.waitKey(10)
height, width, bytesPerComponent = resized1.shape #取彩色图片的长、宽、通道
bytesPerLine = 3 * width
cv.cvtColor(resized1, cv.COLOR_BGR2RGB, resized1)
QImg = QImage(resized1.data, width, height, bytesPerLine,QImage.Format_RGB888)
pixmap = QPixmap.fromImage(QImg)

self.label_ShowPicture.setPixmap(pixmap)
#self.label_ShowPicture.setPixmap(QPixmap("resized1.jpg"))
self.label_ShowPicture.setCursor(Qt.CrossCursor)
print("已经嵌入")
