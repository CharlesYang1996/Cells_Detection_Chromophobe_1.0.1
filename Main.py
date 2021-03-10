#feature_1
#feature_3
#data_smooth_new_try_1_4_1
#feature_4
import cv2 as cv

from feature_1 import step1
#from feature_3_1_10_17 import step2 as step2_1
from feature_3 import step2
from data_smooth_new_try_1_4_3 import step3
from feature_4 import step4
from feature_4_all import step5
import numpy as np
import time

from PIL import Image
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.messagebox

def main(read_type):
    start_time = time.clock()
    not_circle_rate=[]
    non_circle_rate_list=[]
    Cells_quantity,Cells_density=step1(read_type)

    print(Cells_quantity)
    for i in range(1,Cells_quantity):
        try:
            print("System is working on No: ",i," Cell. Total cells: ",Cells_quantity)
            step2(i)


            step3(i)

            non_circle_rate_list.append(step4(i))
            step5(i,Cells_quantity,not_circle_rate)

            #copyfile("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\ouput_marked.bmp","G:\\2020summer\\Project\\Cell_classfication_1.0.0\\output\\"+str(i)+".bmp")
        except:
            pass
    display=cv.imread("bin\\output\\temp_display.bmp")
    dateandtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    cv.putText(display, dateandtime, (80, 60), cv.FONT_HERSHEY_SIMPLEX, 0.5,
               (0, 0, 0), 1)
    cv.putText(display, "Result Value:"+str(np.mean(non_circle_rate_list)), (80, display.shape[0]-400), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv.putText(display, "The lower the value, the higher the probability of Chromophobe", (80, display.shape[0]-350), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv.putText(display, "Total cells number: "+str(Cells_quantity), (80, display.shape[0]-300), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)
    cv.putText(display, "Total cells density: "+str(Cells_density), (80, display.shape[0]-250), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)
    r1 = cv.imread("result\\overview_result1.bmp")
    r2 = cv.imread("result\\cell_clean.bmp")
    cv.imshow("Overview", r1)
    cv.imshow("cell_clean", r2)
    cv.imshow("Final output", display)
    cv.imwrite("result\\Final_Result.bmp", display)
    print("===================Result===================")
    print("cells density : ", Cells_density)

    print("not_circle_rate : ",np.mean(non_circle_rate_list))
    print(np.mean(non_circle_rate_list))
    stop_time = time.clock()
    cost = stop_time - start_time
    print("%s cost %s second" % (os.path.basename(sys.argv[0]), cost))

    plt.hist(non_circle_rate_list,bins=20)
    plt.title('non_circle_rate')
    plt.show()
    shutil.rmtree("output_single")
    os.mkdir("output_single")
    cv.waitKey()

    #write
    '''
    from xlutils.copy import copy 
    rb = xlrd.open_workbook("G:\\2020summer\\Project\\test_report1.xls")  # 打开weng.xls文件
    wb = copy(rb)  # 利用xlutils.copy下的copy函数复制
    ws = wb.get_sheet(0)  # 获取表单0
    ws.write(read_type, 1, Cells_density)  # 改变（0,0）的值
    ws.write(read_type, 2, np.mean(not_circle_rate))  # 增加（8,0）的值
    wb.save("G:\\2020summer\\Project\\test_report1.xls")
    '''




import os,shutil
def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile) #􀠶􂿫􁮷􀔦􀨽􀪼􄐟􁖴
        if not os.path.exists(fpath):
            os.makedirs(fpath) #􀡋􁔪􄐟􁖴
        shutil.move(srcfile,dstfile) #􃀫􀣘􁮷􀔦
        print ("move %s -> %s"%( srcfile,dstfile))
def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:

        fpath,fname=os.path.split(dstfile) #􀠶􂿫􁮷􀔦􀨽􀪼􄐟􁖴
        if not os.path.exists(fpath):
            os.makedirs(fpath) #􀡋􁔪􄐟􁖴
        shutil.copyfile(srcfile,dstfile) #􀼽􀡦􁮷􀔦
        print ("copy %s -> %s"%( srcfile,dstfile))


from PIL import Image
def convert2pdf():
    tkinter.messagebox.showinfo('提示', 'PDF has downloaded in to result_pdf dir')
def closeallwindows():
    cv.destroyAllWindows()
    plt.close()

root = Tk()
path = StringVar()
sw = root.winfo_screenwidth()

sh = root.winfo_screenheight()

ww = 350
wh = 160

x = (sw-ww) / 2
y = (sh-wh) / 2
root.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
root.title("Cancer detect")
Label(root,text = "Path:").grid(row = 0, column = 0)
Entry(root, textvariable = path).grid(row = 0, column = 1)

Button(root, text = "Start", command =lambda :main(0) ).grid(row = 0, column = 2)
#Button(root, text = "Close All Windows", command =lambda :closeallwindows() ).grid(row = 0, column = 3)
Button(root, text = "Download PDF", command =lambda :convert2pdf() ).grid(row = 0, column = 4)

from PIL import Image, ImageTk

'''img_open = Image.open('result\\Final_Result.bmp')
img_png = ImageTk.PhotoImage(img_open)
label_img = Label(root, image = img_png).grid(row = 1, column = 1)
'''
root.mainloop()