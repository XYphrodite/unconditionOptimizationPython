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
    x1 = -10
    x2 = -10
    while (True):
        y1 = fooA(x1, x2)
        y2 = fooA(x1 + dlt, x2)
        horpoints = 0
        verpoints = 0
        if y1 >= y2:
            x1 += dlt
            while y1 >= y2:
                # print("1")
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
                # print("2")
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
                # print("3")
                verpoints -= 1
                y1 = fooA(x1, x2)
                x2 -= dlt
                y2 = fooA(x1, x2)
            x2 += dlt
            verpoints += 1
        else:
            while y1 < y2:
                # print("4")
                # print("x1 = ", x1, " x2 = ", x2 - d, " f = ", fooA(x1, x2 - d))
                verpoints += 1
                y2 = fooA(x1, x2)
                x2 += dlt
                y1 = fooA(x1, x2)
            x2 -= dlt
            verpoints -= 1
        # print([x1, x2])
        # print(horpoints)
        # print(verpoints)

        dc = 0
        tc = 0
        y1 = fooA(x1, x2)
        y2 = fooA(x1 + dlt * horpoints / 100, x2 + dlt * verpoints / 100)
        if y1 < y2:
            while y1 < y2:
                dc += 1
                # print([x1, x2, y1, y2])
                y2 = fooA(x1, x2)
                x1 -= dlt * horpoints
                x2 -= dlt * verpoints
                y1 = fooA(x1, x2)
            x1 += dlt * horpoints
            x2 += dlt * verpoints

        if y1 > y2:
            while y1 > y2:
                tc += 1
                # print([x1, x2, y1, y2])
                y1 = fooA(x1, x2)
                x1 -= dlt * horpoints
                x2 -= dlt * verpoints
                y2 = fooA(x1, x2)
            x1 += dlt * horpoints
            x2 += dlt * verpoints
        if (math.fabs(horpoints) <= 2) and (math.fabs(verpoints) <= 2) and ((dc <= 2) or (tc <= 2)):
            return [x1, x2]


def symplex(E):
    def l3(arr):
        return arr[2]

    maxK = 100000
    n = 2
    a = 1
    b = 2
    g = 0.5
    k = 0.5
    x1 = [-2, -4, 0]
    x2 = [x1[0] + x1[0] * k, x1[1], 0]
    x3 = [x1[0], x1[1] + x1[1] * k, 0]
    x1[2] = fooA(x1[0], x1[1])
    x2[2] = fooA(x2[0], x2[1])
    x3[2] = fooA(x3[0], x3[1])
    x = [x1, x2, x3]

    sig2 = 0
    for i in range(1, n + 1):
        ff = 0
        for j in range(1, n + 1):
            ff += x[j][2] / (n + 1)
        sig2 += pow(x[i][2] - ff, 2) / (n + 1)

    while (sqrt(sig2) >= e):
        x1[2] = fooA(x1[0], x1[1])
        x2[2] = fooA(x2[0], x2[1])
        x3[2] = fooA(x3[0], x3[1])
        x.sort(key=l3)

        xc = [(x[0][0] + x[1][0]) / n, (x[0][1] + x[1][1]) / n, 0]
        xc[2] = fooA(xc[0], xc[1])
        y0 = fooA(xc[0] - xc[2], xc[1] - xc[2])
        x0 = [(1 + a) * xc[0] - a * x[2][0], (1 + a) * xc[1] - a * x[2][1], 0]
        x0[2] = fooA(x0[0], x0[1])
        y0 = fooA(x0[0] - y0, x0[1] - y0)
        if (y0 < x[0][2]):
            xr = [(1 - b) * xc[0] - b * x0[0], (1 - b) * xc[1] - b * x0[1], 0]
            xr[2] = fooA(xr[0], xr[1])
            yr = fooA(xr[0] - xr[2], xr[1] - xr[2])
            if (yr < y0):
                x[2] = xr
            else:
                x[2] = x0
        elif (y0 <= x[1][2]):
            x[2] = x0
        elif (y0 < x[2][2]):
            xg = [(1 - g) * xc[0] + g * x0[0], (1 - g) * xc[1] + g * x0[1], 0]
            xg[2] = fooA(xg[0], xg[1])
            yg = fooA(xg[0] - xg[2], xg[1] - xg[2])
            if (yg < x[2][2]):
                x[2] = xg
        else:
            xg = [(1 - g) * xc[0] + g * x[2][0], (1 - g) * xc[1] + g * x[2][1], 0]
            xg[2] = fooA(xg[0], xg[1])
            yg = fooA(xg[0] - xg[2], xg[1] - xg[2])
            if (yg < x[2][2]):
                x[2] = xg
            else:
                for i in range(1, n + 1):
                    x[i][0] = x[i][0] - (x[i][0] - x[0][0]) / 2
                    x[i][1] = x[i][1] - (x[i][1] - x[0][1]) / 2

        sig2 = 0
        for i in range(1, n + 1):
            ff = 0
            for j in range(1, n + 1):
                ff += x[j][2] / (n + 1)
            sig2 += pow(x[i][2] - ff, 2) / (n + 1)
        maxK -= 1
        if (maxK <= 0): break

    return [(x[0][0] + x[1][0] + x[2][0]) / 3, (x[0][1] + x[1][1] + x[2][1]) / 3]


print("Start:")
print("Powel = ", powel())
print("Symplex = ", symplex(E))