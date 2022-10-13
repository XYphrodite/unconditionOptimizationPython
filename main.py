import math
from math import *

# consts

E = 0.01
dlt = E / 10


def fooA(x1, x2):
    a = 6
    b = -1
    c = 3
    d = 4
    alf = 70
    return (pow(((x1 - a) * cos(alf) + (x2 - b) * sin(alf)), 2)) / (c * c) + \
           (pow(((x2 - b) * cos(alf) - (x1 - a) * sin(alf)), 2)) / (d * d)


def powel():
    x1 = -10
    x2 = 8

    while (True):
        y1 = fooA(x1, x2)
        y2 = fooA(x1 - dlt, x2)
        horpoints = 0
        verpoints = 0
        if y1 >= y2:
            while y1 >= y2:
                # print("x1 = ", x1, " x2 = ", x2, " f1 = ", y1, " f2 = ", y2)
                horpoints -= 1
                y1 = fooA(x1, x2)
                x1 -= dlt
                y2 = fooA(x1, x2)
            x1 -= dlt
            horpoints += 1
        else:
            while y1 > y2:
                # print("x1 = ", x1, " x2 = ", x2, " f1 = ", y1, " f2 = ", y2)

                horpoints += 1
                y1 = fooA(x1, x2)
                x1 += dlt
                y2 = fooA(x1, x2)
            x1 += dlt
            horpoints -= 1
        # print([x1, x2])
        y1 = fooA(x1, x2)
        y2 = fooA(x1, x2 - dlt)
        if y1 >= y2:
            while y1 >= y2:
                # print("x1 = ", x1, " x2 = ", x2, " f = ", fooA(x1, x2))
                print("34rtv c")

                verpoints -= 1
                y1 = fooA(x1, x2)
                x2 -= dlt
                y2 = fooA(x1, x2)
            x2 += dlt
            verpoints += 1
        else:
            while y1 > y2:
                # print("x1 = ", x1, " x2 = ", x2 - d, " f = ", fooA(x1, x2 - d))
                verpoints += 1
                y1 = fooA(x1, x2)
                x2 += dlt
                y2 = fooA(x1, x2)
            x2 -= dlt
            verpoints -= 1
        # print([x1, x2])
        print(horpoints)
        print(verpoints)

        if (math.fabs(horpoints) <= 2) and (math.fabs(verpoints) <= 2):
            return [x1, x2]

        y1 = fooA(x1, x2)
        y2 = fooA(x1 + dlt * horpoints / 100, x2 + dlt * verpoints / 100)
        if y1 > y2:
            while y1 > y2:
                print("wnjefd c")
                y1 = fooA(x1, x2)
                x1 -= dlt * horpoints / 100
                x2 -= dlt * verpoints / 100
                y2 = fooA(x1, x2)
            x1 += dlt * horpoints / 100
            x2 += dlt * verpoints / 100
        elif y1 < y2:
            while y1 < y2:
                print("werf")
                y1 = fooA(x1, x2)
                x1 += dlt * horpoints / 100
                x2 += dlt * verpoints / 100
                y2 = fooA(x1, x2)
            x1 += dlt * horpoints / 100
            x2 += dlt * verpoints / 100
        else:
            return [x1, x2]

        print([x1, x2])


print("Start:")
print("Powel = ", powel())
