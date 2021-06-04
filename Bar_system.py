import cv2 as cv

def set_Bar(Result_Value_bar):
    img1 = cv.imread('bin\\output\\temp_display.bmp')
    # img_bar = cv.imread('bin\\bar.png')

    # print("Img size: [Width :",img1.shape[0],"]","[Height :",img1.shape[1],"]")
    #cv.imwrite("result\\overview_result1.bmp", img_masked)
    # print("============Step 1 End============")
    try:
        # x_offset=round(319+62*Result_Value_bar)
        # y_offset=22
        # img1[y_offset:y_offset+img_bar.shape[0], x_offset:x_offset+img_bar.shape[1]] = img_bar

        # start_point = (200, 260)
        #
        # end_point = (start_point[0] + 200, start_point[1] + 20)
        #
        # color = (255, 0, 0)
        #
        # thickness = 2
        #
        # image = cv.rectangle(img1, start_point, end_point, color, thickness)
        cv.imwrite("bin\\bar.png", img1)
    except:
        print("Bar print error!")
        pass
    # cv.imshow("1", image )

    #cv.waitKey()

if __name__ == '__main__':

    set_Bar(3.33)
