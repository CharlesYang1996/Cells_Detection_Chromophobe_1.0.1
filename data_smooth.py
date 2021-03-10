import math
def quantile_p(data, p):
    pos = (len(data) + 1)*p
    #pos = 1 + (len(data)-1)*p
    pos_integer = int(math.modf(pos)[1])
    pos_decimal = pos - pos_integer
    Q = data[pos_integer - 1] + (data[pos_integer] - data[pos_integer - 1])*pos_decimal
    return Q
def outliers_detect(data):

    Q1 = quantile_p(data, 0.25)

    Q2 = quantile_p(data, 0.5)

    Q3 = quantile_p(data, 0.75)

    IQR=Q3-Q1
    min_line=int(round(Q1-1.5*IQR))
    max_line=int(round(Q3+1.5*IQR))
    print("Top outlier line is : ",max_line," Bot outlier line is : ",min_line)
    return max_line,min_line

