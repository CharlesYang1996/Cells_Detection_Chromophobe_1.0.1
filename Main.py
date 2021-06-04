#feature_1
#feature_3
#data_smooth_new_try_1_4_1
#feature_4
from tkinter import filedialog

import cv2 as cv

from feature_1 import step1
#from feature_3_1_10_17 import step2 as step2_1
from feature_3 import step2
from data_smooth_new_try_1_4_3 import step3
from feature_4 import step4
from feature_4_all import step5
import numpy as np
import time
from Bar_system import set_Bar
from PIL import Image
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.messagebox

# place your directory here
path_slides = r'F:\YI RONG\BU\Research-resources\CellDetection\Cells_Detection_Chromophobe_1.0.1\test_image\\Oncocytoma'

def main(read_type, path_slides = ''):
    # read type:
    # 0: read a file, 1: read all images in a directory
    if read_type == 0:
        file_path = filedialog.askopenfilename()
        detector(file_path)

    elif read_type == 1:
        directory = path_slides
        for filename in os.listdir(directory):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                print(os.path.join(directory, filename))
                file_path = os.path.join(directory, filename)
                detector(file_path)
            else:
                continue

def detector(path_slides = ''):
    start_time = time.time()
    not_circle_rate=[]
    non_circle_rate_list=[]

    Cells_quantity, Cells_density, Cell_nucleus_color = step1(path_slides)

    # print(Cells_quantity)
    for i in range(1, Cells_quantity):
        try:
            # print("System is working on No: ", i + 1, " Cell. Total cells: ", Cells_quantity)

            step2(i)

            step3(i)

            non_circle_rate_list.append(step4(i))
            step5(i, Cells_quantity, not_circle_rate)

            #copyfile("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\ouput_marked.bmp","G:\\2020summer\\Project\\Cell_classfication_1.0.0\\output\\"+str(i)+".bmp")
        except:
            pass
    display = cv.imread("bin\\output\\temp_display.bmp")
    dateandtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    stop_time = time.time()
    cost = stop_time - start_time
    V_1 = float(Cells_density)
    V_2 = float(Cell_nucleus_color)
    V_3 = float(np.mean(non_circle_rate_list))
    #Result
    Result_value = round((1 * ((V_1 - 0.865) / 0.282) + 1 * ((V_2 - 179.229) / 1.874) + 2 * ((V_3 - 0.234) / 0.030)), 3)
    # Result_value = round(-1*(2*((V_1-1)/0.7)+1*((165-V_2)/35)+2*((V_3-0.25)/0.06)),3)
    #Bar
    set_Bar(Result_value)
    x_offset1 = 210
    y_offset1 = display.shape[0]-390
    img_bar = cv.imread('bin\\bar.png')
    barx, bary = img_bar.shape[0:2]
    img_bar1 = cv.resize(img_bar, (int(bary / 2), int(barx / 2)))
    # display[y_offset1:y_offset1 + img_bar1.shape[0], x_offset1:x_offset1 + img_bar1.shape[1]] = img_bar1

    #Text
    cv.putText(display, dateandtime, (80, 60), cv.FONT_HERSHEY_SIMPLEX, 0.5,
               (0, 0, 0), 1)
    cv.putText(display, "Result Value:" + str(Result_value), (80, display.shape[0]-400), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    if Result_value >= 0:
        cv.putText(display, "Detection Reslut: Oncocytoma", (80, display.shape[0]-350), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    else:
        cv.putText(display, "Dection Reslut: Chromophobe", (80, display.shape[0] - 350), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv.putText(display, "Total cells number: "+str(Cells_quantity), (80, display.shape[0]-300), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv.putText(display, "Total cells density: "+str(Cells_density), (80, display.shape[0]-250), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv.putText(display, "Aveage cell nucleus color depth: " + str(round(Cell_nucleus_color,3)), (80, display.shape[0] - 200),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv.putText(display, "Non-circle Value:" + str(round(np.mean(non_circle_rate_list),3)), (80, display.shape[0] - 150),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv.putText(display, "Running time: " + str(round(cost)) + " second", (80, display.shape[0] - 10), cv.FONT_HERSHEY_SIMPLEX,
               0.5, (0, 0, 0), 1)
    # cv.putText(display, "Running time: " + str(cost)+" second", (80, display.shape[0] - 100),cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)
    # r1 = cv.imread("bin\\overview_result1.bmp")
    # r2 = cv.imread("bin\\cell_clean.bmp")
    # cv.imshow("Overview", r1)
    # cv.imshow("cell_clean", r2)
    cv.imshow("Final output", display)
    cv.imwrite("bin\\output\\Final_Result.bmp", display)
    print("===================Result===================")
    print("result value : ", Result_value)
    print("cells density : ", Cells_density)

    print("not_circle_rate : ",np.mean(non_circle_rate_list))

    print("Cell nucleus color depth : ", Cell_nucleus_color)
    print("%s cost %s second" % (os.path.basename(sys.argv[0]), cost))

    plt.hist(non_circle_rate_list,bins=20)
    plt.title('non_circle_rate')
    plt.show()
    # shutil.rmtree("bin\\output_single")
    # os.mkdir("bin\\output_single")
    # cv.waitKey()

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

Button(root, text = "Start", command =lambda :main(0,
path_slides)).grid(row = 0, column = 2)
#Button(root, text = "Close All Windows", command =lambda :closeallwindows() ).grid(row = 0, column = 3)
Button(root, text = "Download PDF", command =lambda :convert2pdf() ).grid(row = 0, column = 4)

from PIL import Image, ImageTk

'''img_open = Image.open('bin\\output\\Final_Result.bmp')
img_png = ImageTk.PhotoImage(img_open)
label_img = Label(root, image = img_png).grid(row = 1, column = 1)
'''
root.mainloop()