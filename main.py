import math
from math import *
import numpy as np

E = 0.01
dlt = E / 100


def foo(x1, x2, n):
    if n == 0:
        a = 6
        b = -1
        c = 3
        d = 4
        alf = 70
        return (pow(((x1 - a) * cos(alf) + (x2 - b) * sin(alf)), 2)) / (c * c) + \
               (pow(((x2 - b) * cos(alf) - (x1 - a) * sin(alf)), 2)) / (d * d)
    else:
        return 100 * pow((x2 - pow(x1, 2)), 2) + pow((1 - x1), 2)


def powell(dlt, n):
    x1 = 0
    x2 = 0
    while (True):
        y1 = foo(x1, x2, n)
        y2 = foo(x1 + dlt, x2, n)
        horpoints = 0
        verpoints = 0
        if y1 >= y2:
            x1 += dlt
            while y1 >= y2:
                # print("1")
                horpoints -= 1
                y1 = foo(x1, x2, n)
                x1 += dlt
                y2 = foo(x1, x2, n)
            x1 -= dlt
            horpoints += 1
        else:
            x1 -= dlt
            while y1 < y2:
                # print("2")
                horpoints += 1
                y2 = foo(x1, x2, n)
                x1 -= dlt
                y1 = foo(x1, x2, n)
            x1 += dlt
            horpoints -= 1
        # print([x1, x2])
        y1 = foo(x1, x2, n)
        y2 = foo(x1, x2 - dlt, n)
        if y1 >= y2:
            while y1 >= y2:
                # print("3")
                verpoints -= 1
                y1 = foo(x1, x2, n)
                x2 -= dlt
                y2 = foo(x1, x2, n)
            x2 += dlt
            verpoints += 1
        else:
            while y1 < y2:
                # print("4")
                verpoints += 1
                y2 = foo(x1, x2, n)
                x2 += dlt
                y1 = foo(x1, x2, n)
            x2 -= dlt
            verpoints -= 1
        # print([x1, x2])
        # print(horpoints)
        # print(verpoints)
        dc = 0
        tc = 0
        y1 = foo(x1, x2, n)
        y2 = foo(x1 + dlt * horpoints / 100, x2 + dlt * verpoints / 100, n)
        if y1 < y2:
            while y1 < y2:
                dc += 1
                # print([x1, x2, y1, y2])
                y2 = foo(x1, x2, n)
                x1 -= dlt * horpoints
                x2 -= dlt * verpoints
                y1 = foo(x1, x2, n)
            x1 += dlt * horpoints
            x2 += dlt * verpoints

        if y1 > y2:
            while y1 > y2:
                tc += 1
                # print([x1, x2, y1, y2])
                y1 = foo(x1, x2, n)
                x1 -= dlt * horpoints
                x2 -= dlt * verpoints
                y2 = foo(x1, x2, n)
            x1 += dlt * horpoints
            x2 += dlt * verpoints
        if (math.fabs(horpoints) <= 2) and (math.fabs(verpoints) <= 2) and ((dc <= 2) or (tc <= 2)):
            return [x1, x2]


def FindGCenter(p, n):
    xc = [(p[0][0] + p[1][0]) / 2, (p[0][1] + p[1][1]) / 2, 0]
    xc[2] = foo(xc[0], xc[1], n)
    return xc


def symplex(dlt, n):
    def y(arr):
        return arr[2]

    N = 2
    a = 1
    b = 0.5
    g = 2
    k = 0.5
    #####################################
    # задаётся n+1 точка
    #    x1  x2 f
    p1 = [0, 0, 0]
    p2 = [1, 0, 0]
    p3 = [0, 1, 0]
    # вычесляются y-ки
    p1[2] = foo(p1[0], p1[1], n)
    p2[2] = foo(p2[0], p2[1], n)
    p3[2] = foo(p3[0], p3[1], n)
    p = [p1, p2, p3]

    ff = (p[0][2] + p[1][2] + p[2][2]) / 3
    sig2 = (pow(p[0][2] - ff, 2) + pow(p[1][2] - ff, 2) + pow(p[2][2] - ff, 2)) / 3
    # находим h, g, l
    while (sqrt(sig2) >= dlt):
        # вычесляются y-ки
        p1[2] = foo(p1[0], p1[1], n)
        p2[2] = foo(p2[0], p2[1], n)
        p3[2] = foo(p3[0], p3[1], n)
        p.sort(key=y)
        # определяем центр тяжести всех точек кроме h
        xc = FindGCenter(p, n)

        xr = [xc[0] + a * (xc[0] - p[2][0]), xc[1] + a * (xc[1] - p[2][1]), 0]
        xr[2] = foo(xr[0], xr[1], n)

        if (xr[2] < p[2][2]):
            xe = [xc[0] + g * (xc[0] - p[2][0]), xc[1] + g * (xc[1] - p[2][1]), 0]
            xe[2] = foo(xe[0], xe[1], n)
            # растяжение
            if (xe[2] < p[2][2]): #f0<fl
                p[2] = xe
            # отражение
            else:
                p[2] = xr
            # отражение
        elif (xr[2] < p[1][2]):
            p[2] = xr
        elif (xr[2] < p[2][2]):
            xcon = [xc[0] + b * (xc[0] - p[2][0]), xc[1] + b * (xc[1] - p[2][1]), 0]
            xcon[2] = f(xcon[0], xcon[1])
            # outside contract
            if (xcon[2] <= xr):
                p[2] = xcon
            # уменьшение
            else:
                for i in range(1, N + 1):
                    x[i][0] = (x[i][0] + x[0][0]) / 2
                    x[i][1] = (x[i][1] + x[0][1]) / 2
                    x[i][2] = f(x[i][0], x[i][1])
        else:
            xcon = [xc[0] + b * (p[2][0] - xc[0]), xc[1] + b * (p[2][1] - xc[1]), 0]
            xcon[2] = foo(xcon[0], xcon[1], n)
            # inside contract
            if (xcon[2] < p[2][2]):
                p[2] = xcon
            # shrink
            else:
                for i in range(1, N + 1):
                    p[i][0] = (p[i][0] + p[0][0]) / 2
                    p[i][1] = (p[i][1] + p[0][1]) / 2
                    p[i][2] = foo(p[i][0], p[i][1], n)

        ff = (p[0][2] + p[1][2] + p[2][2]) / 3
        sig2 = (pow(p[0][2] - ff, 2) + pow(p[1][2] - ff, 2) + pow(p[2][2] - ff, 2)) / 3

    return [(p[0][0] + p[1][0] + p[2][0]) / 3, (p[0][1] + p[1][1] + p[2][1]) / 3]


print("Start:")
print("Powell a) = ", powell(dlt, 0))
print("Powell b) = ", powell(dlt / 42, 1))
print("Symplex a) = ", symplex(dlt, 0))
print("Symplex b) = ", symplex(dlt / 42, 1))


