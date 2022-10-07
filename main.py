import numpy as M

# consts
a = 6
b = -1
c = 3
d = 4
alpha = 70
E = 0.01
d = E / 10


def fooA(x1, x2):
    return pow(((x1 - a) * M.cos(70) + (x2 - b) * M.sin(alpha)) / c, 2) + pow(
        ((x2 - b) * M.cos(alpha) - (x1 - a) * M.sin(alpha)) / d, 2)


def powel():
    horpoints = 0
    verpoints = 0
    x1 = -5
    x2 = 5

    while fooA(x1, x2) <= fooA(x1 + d, x2):
        print("x1 = ", x1, "f = ", fooA(x1, x2))
        x1 += d
        horpoints += 1
    while fooA(x1, x2) > fooA(x1 - d, x2):
        print("left")
        x1 -= d
        horpoints -= 1
    while fooA(x1, x2) <= fooA(x1, x2 + d):
        print("top")
        x2 += d
        verpoints += 1
    while fooA(x1, x2) > fooA(x1, x2 - d):
        print("down")
        x2 -= d
        verpoints -= 1
    while fooA(x1, x2) > fooA(x1 + d * horpoints, x2 + d * verpoints):
        print("diag")
        x1 += d * horpoints
        x2 += d * verpoints
    return [x1, x2]


print("Start:")
print(powel())
