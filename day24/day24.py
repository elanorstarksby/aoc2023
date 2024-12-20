import datetime
from collections import namedtuple
import sympy as sym


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip().split(" @ ") for line in input_file]
    return lines


TEST_AREA = (200000000000000, 400000000000000)


# TEST_AREA = (7, 27)


def make_lines(values):
    lines = []
    for line_description in values:
        [xs, ys] = line_description[0].split(", ")[0:2]
        x, y = int(xs), int(ys)
        [vxs, vys] = line_description[1].split(", ")[0:2]
        vx, vy = int(vxs), int(vys)
        # print(x, y, vx, vy)
        # y = mx + c
        # c = y - mx = y - (vy/vx) * x
        # input has no vx or vy 0
        if vx == 0 or vy == 0:
            print("Zero not expect:", line_description)
        m = vy / vx
        c = y - m * x
        lines.append((m, c, vx, x))
    return lines


def p1(values):
    lines = make_lines(values)

    intersections = 0
    while lines:
        (m1, c1, vx1, x1) = lines.pop()
        for (m2, c2, vx2, x2) in lines:
            # m1 * x + c1 = m2 * x + c2
            # x (m1 - m2) = c2 - c1
            # x = (c2 - c1) / (m1 - m2)
            if m1 == m2:
                continue
            x = (c2 - c1) / (m1 - m2)
            y = m1 * x + c1
            if TEST_AREA[0] <= x <= TEST_AREA[1] and TEST_AREA[0] <= y <= TEST_AREA[1]:
                if (vx1 > 0 and x > x1) or (vx1 < 0 and x < x1):
                    if (vx2 > 0 and x > x2) or (vx2 < 0 and x < x2):
                        # print(x, y)
                        intersections += 1

    return intersections


Line = namedtuple('Line', 'x y z vx vy vz')


def p2(values):
    eqs = []
    t = sym.symbols(','.join(f'tr{i + 1}' for i in range(3)))
    # print(t)
    xr, yr, zr = sym.symbols('xr,yr,zr')
    vxr, vyr, vzr = sym.symbols('vxr,vyr,vzr')
    for i in range(3):
        line_description = values[i]
        start = line_description[0].split(", ")
        [xi, yi, zi] = [int(a) for a in start]
        vel = line_description[1].split(", ")
        [vxi, vyi, vzi] = [int(a) for a in vel]

        eq = sym.Eq(xi + vxi * t[i], xr + vxr * t[i])
        # print(eq)
        eqs.append(eq)
        eq = sym.Eq(yi + vyi * t[i], yr + vyr * t[i])
        eqs.append(eq)
        eq = sym.Eq(zi + vzi * t[i], zr + vzr * t[i])
        eqs.append(eq)
    result = sym.solve(eqs, (xr, yr, zr, vxr, vyr, vzr, *t))[0]
    # print(result)
    return sum(result[0:3])


def main():
    values = read_in()
    # print(p1(values))
    t = datetime.datetime.now()
    print(p2(values))
    print(datetime.datetime.now() - t)


if __name__ == '__main__':
    main()
