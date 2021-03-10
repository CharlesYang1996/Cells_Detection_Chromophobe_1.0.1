
import math

#print ("cos(3) : ",  math.cos(3))
#print ("cos(-3) : ",  math.cos(-3))
#print ("cos(0) : ",  math.cos(0))
#print ("cos(math.pi) : ",  math.cos(math.pi))
#print ("cos(2*math.pi) : ",  math.cos(2*math.pi))
#print ("sin(1/6*math.pi) : ",  math.sin(1/6*math.pi))

def angle_round(cx,cy,d):
    angle_round_list=[]
    angle_unit_number=36 #一个pi分成18份，没一份10度"
    #print("Warning: A circle is divided into ",angle_unit_number," parts, each part of ",round(180/angle_unit_number,1)," degrees")
    for i in range(1,angle_unit_number*2+1):
        #print (i)
        #print("sin ",i,"/",angle_unit_number," pi = ", round(math.sin(i / angle_unit_number * math.pi),3))
        #print("cos ", i, "/",angle_unit_number," pi = ", round(math.cos(i / angle_unit_number * math.pi), 3))
        x1= round(math.cos(i / angle_unit_number * math.pi), 3) * d + cx
        y1 = round(math.sin(i / angle_unit_number * math.pi), 3) * d + cy
        angle_round_list.append([x1,y1])
    #print(angle_round_list)
    return angle_round_list

def un_angle_round(cx,cy,round_list):

    angle_round_list=[]
    angle_unit_number=36 #一个pi分成18份，没一份10度"
    #print("Warning: A circle is divided into ",angle_unit_number," parts, each part of ",round(180/angle_unit_number,1)," degrees")
    for i in range(1,angle_unit_number*2+1):
        d=round_list[i-1]
        #print (i)
        #print("sin ",i,"/",angle_unit_number," pi = ", round(math.sin(i / angle_unit_number * math.pi),3))
        #print("cos ", i, "/",angle_unit_number," pi = ", round(math.cos(i / angle_unit_number * math.pi), 3))
        x1= round(round(math.cos(i / angle_unit_number * math.pi), 3) * d + cx)

        y1 = round(round(math.sin(i / angle_unit_number * math.pi), 3) * d + cy)
        angle_round_list.append([x1,y1])
    #print(angle_round_list)
    return angle_round_list




def cell_wall_ray_lenth(cx,cy,x1,y1):
    distance=round(((x1-cx)**2+(y1-cy)**2)**0.5,3)
    return distance

a=cell_wall_ray_lenth(0,0,2,0)


def distance(x1,y1,x2,y2):
    result=((x1-x2)**2+(y1-y2)**2)**0.5

    return round(result,2)



def quantile_p(data,p):
    pos = (len(data) + 1)*p
    #pos = 1 + (len(data)-1)*p
    pos_integer = int(math.modf(pos)[1])
    pos_decimal = pos - pos_integer
    Q = data[pos_integer - 1] + (data[pos_integer] - data[pos_integer - 1])*pos_decimal
    return Q

def ourliers_clean(list):#not finished
    list.sort()

    #print(list)
    Q1=quantile_p(list,0.25)
    Q2=quantile_p(list,0.5)
    Q3=quantile_p(list,0.75)
    #print(list)

    IQR=Q3-Q1
    Min_limit=Q1-1.5*IQR
    Max_limit=Q3+1.5*IQR
    #print(" Q1:", Q1, " Q2:", Q2, " Q3:", Q3, "Min_limit:", Min_limit,"Max_limit:",Max_limit)

    for i in range(0,len(list)):
        if list[i]<=Min_limit and list[i]>=Max_limit:
            list.remove(list[i])
    #print(list)
    return list


#ourliers_clean([6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49,1100])

def combine_two_2d_list(a,b):
    for i in range(0, len(a)):
        #print(a[i])

        #print(b[i])
        a[i].append(b[i][0])

    return a

def find_min_length_list(dataset):
    m=999
    for i in dataset:
        if len(i)<=m:
            m=len(i)
            position=dataset.index(i)

    #print(position,dataset[position])
    return position,dataset[position]

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
def GetAreaOfPolyGonbyVector(points):
    # 基于向量叉乘计算多边形面积
    area = 0
    if(len(points)<3):

         raise Exception("error")

    for i in range(0,len(points)-1):
        p1 = points[i]
        p2 = points[i + 1]

        triArea = (p1.x*p2.y - p2.x*p1.y)/2
        area += triArea
    return abs(area)
def area_calculate_from_points(points_list):
    points = []
    x=[]
    y=[]
    for i in range(0,len(points_list)):
        x.append(points_list[i][0])
        y.append(points_list[i][1])
    #x = [1,2,3,4,5,6,5,4,3,2]
    #y = [1,2,2,3,3,3,2,1,1,1]
    for index in range(len(x)):
        points.append(Point(x[index],y[index]))

    area = GetAreaOfPolyGonbyVector(points)
    #print(area)
    #print("The area of this cell is: ",math.ceil(area))
    #assert math.ceil(area)==1
    return math.ceil(area)


def holo_area_calculate_from_points(points_list,img,threshold):
    white_count=0

    for i in range(0,len(points_list)):
        x=points_list[i][0]
        y = points_list[i][1]
        print(img[x,y])

        if img[x,y]>=threshold:
            white_count+=1

    print("The Holo of this cell is: ",white_count)
    return white_count

def find_longest_element_index(list):
    word_len_list = [len(word) for word in list]
    max_word_len = max(word_len_list)
    for word in list:
        if len(word) == max_word_len:
            #print("find_longest_element: ",word)
            output=list.index(word)
            #print("find_longest_element_index:",output)

    return output


def relocate_start_point(units_number, start_point):
    i1 = [tt for tt in range(0, start_point+1)]

    i2 = [t for t in range(start_point+1, units_number)]

    i2.extend(i1)

    return i2