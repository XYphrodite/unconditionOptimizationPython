from math import *

# consts

E = 0.01
dlt = E / 1


def fooA(x1, x2):
    a = 6
    b = -1
    c = 3
    d = 4
    alf = 70
    return (pow(((x1 - a) * cos(alf) + (x2 - b) * sin(alf)), 2)) / (c * c) + \
           (pow(((x2 - b) * cos(alf) - (x1 - a) * sin(alf)), 2)) / (d * d)


def powel():
    x1 = 8
    x2 = 8
    print([x1, x2])
    x1i = x1
    x2i = x2

    while (True):
        y1 = fooA(x1, x2)
        y2 = fooA(x1 - dlt, x2)
        hF = False
        vF = False
        dF = False
        horpoints = 0
        verpoints = 0
        if y1 >= y2:
            hF = True
            while y1 >= y2:
                # print("x1 = ", x1, " x2 = ", x2, " f1 = ", y1, " f2 = ", y2)
                x1 -= dlt
                horpoints -= 1
                y1 = fooA(x1, x2)
                y2 = fooA(x1 - dlt, x2)
            x1 -= dlt
        else:
            hF = True
            while y1 < y2:
                # print("x1 = ", x1, " x2 = ", x2, " f1 = ", y1, " f2 = ", y2)
                x1 += dlt
                horpoints += 1
                y1 = fooA(x1, x2)
                y2 = fooA(x1 - dlt, x2)
            x1 += dlt
        print([x1, x2])
        y1 = fooA(x1, x2)
        y2 = fooA(x1, x2 - dlt)
        if y1 >= y2:
            vF = True
            while y1 >= y2:
                # print("x1 = ", x1, " x2 = ", x2, " f = ", fooA(x1, x2))
                # print("x1 = ", x1, " x2 = ", x2 - d, " f = ", fooA(x1, x2-d))

                verpoints -= 1
                y1 = fooA(x1, x2)
                x2 -= dlt
                y2 = fooA(x1, x2)

        else:
            vF = True
            while y1 < y2:
                # print("x1 = ", x1, " x2 = ", x2 - d, " f = ", fooA(x1, x2 - d))

                verpoints += 1
                y1 = fooA(x1, x2)
                x2 += dlt
                y2 = fooA(x1, x2)
        print([x1, x2])
        print(horpoints)
        print(verpoints)

        x1 = x1i
        x2 = x2i
        y1 = fooA(x1, x2)
        y2 = fooA(x1 + dlt * horpoints, x2 + dlt * verpoints)
        while y1 >= y2:
            dF = True
            print("x1 = ", x1, " x2 = ", x2, " f = ", y1, " f2 ",y2 )
            y1 = fooA(x1, x2)
            x1 += dlt * horpoints/100
            x2 += dlt * verpoints/100
            y2 = fooA(x1, x2)
        #if (hF == False) and (vF == False) and (dF == False):
        return [x1, x2]


print("Start:")
print("Powel = ",powel())
