import math
from math import *

# consts

E = 0.01
dlt = E / 100


def fooA(x1, x2):
    a = 6
    b = -1
    c = 3
    d = 4
    alf = 70
    return (pow(((x1 - a) * cos(alf) + (x2 - b) * sin(alf)), 2)) / (c * c) + \
           (pow(((x2 - b) * cos(alf) - (x1 - a) * sin(alf)), 2)) / (d * d)


def powel():
    x1 = 5
    x2 = 99
    while (True):
        y1 = fooA(x1, x2)
        y2 = fooA(x1 + dlt, x2)
        horpoints = 0
        verpoints = 0
        if y1 >= y2:
            x1 += dlt
            while y1 >= y2:
                #print("1")
                horpoints -= 1
                y1 = fooA(x1, x2)
                x1 += dlt
                y2 = fooA(x1, x2)
            x1 -= dlt
            horpoints += 1
        else:
            x1 -= dlt
            while y1 < y2:
                # print("x1 = ", x1, " x2 = ", x2, " f1 = ", y1, " f2 = ", y2)
                #print("2")
                horpoints += 1
                y2 = fooA(x1, x2)
                x1 -= dlt
                y1 = fooA(x1, x2)
            x1 += dlt
            horpoints -= 1
        # print([x1, x2])
        y1 = fooA(x1, x2)
        y2 = fooA(x1, x2 - dlt)
        if y1 >= y2:
            while y1 >= y2:
                # print("x1 = ", x1, " x2 = ", x2, " f = ", fooA(x1, x2))
                #print("3")
                verpoints -= 1
                y1 = fooA(x1, x2)
                x2 -= dlt
                y2 = fooA(x1, x2)
            x2 += dlt
            verpoints += 1
        else:
            while y1 > y2:
                #print("4")
                # print("x1 = ", x1, " x2 = ", x2 - d, " f = ", fooA(x1, x2 - d))
                verpoints += 1
                y1 = fooA(x1, x2)
                x2 += dlt
                y2 = fooA(x1, x2)
            x2 -= dlt
            verpoints -= 1
        # print([x1, x2])
        #print(horpoints)
        #print(verpoints)

        dc = 0
        tc = 0
        y1 = fooA(x1, x2)
        y2 = fooA(x1 + dlt * horpoints / 100, x2 + dlt * verpoints / 100)
        if y1 < y2:
            while y1 < y2:
                dc += 1
                #print([x1, x2, y1, y2])
                y2 = fooA(x1, x2)
                x1 -= dlt * horpoints
                x2 -= dlt * verpoints
                y1 = fooA(x1, x2)
            x1 += dlt * horpoints
            x2 += dlt * verpoints

        if y1 > y2:
            while y1 > y2:
                tc += 1
                #print([x1, x2, y1, y2])
                y1 = fooA(x1, x2)
                x1 -= dlt * horpoints
                x2 -= dlt * verpoints
                y2 = fooA(x1, x2)
            x1 += dlt * horpoints
            x2 += dlt * verpoints
        if (math.fabs(horpoints) <= 2) and (math.fabs(verpoints) <= 2) and ((dc <= 2) or (tc <= 2)):
            return [x1, x2]

def symplex():
    

print("Start:")
print("Powel = ", powel())
