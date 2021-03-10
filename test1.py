import xlrd
import os
import numpy as np

from xlutils.copy import copy
rb = xlrd.open_workbook("G:\\2020summer\\Project\\nucleus_color.xls")  # 打开.xls文件
wb = copy(rb)  # 利用xlutils.copy下的copy函数复制
ws = wb.get_sheet(0)  # 获取表单0
ws.write(1, 1," numpy.mean(Whole_pic_cell_color_ave)")  # 改变（0,0）的值
# ws.write(read_type, 2, np.mean(not_circle_rate))  # 增加（8,0）的值
wb.save("G:\\2020summer\\Project\\nucleus_color.xls")