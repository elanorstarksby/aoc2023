import copy
import datetime

BILLION = 1000000000


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def p1(values):
    rocks = {}
    total = 0
    l = len(values)
    for row in range(len(values)):
        for col in range(len(values[row])):
            if values[row][col] == "O":
                r = row
                while r > 0 and (r - 1, col) not in rocks:
                    r -= 1
                rocks[(r, col)] = "O"
                total += l - r
            elif values[row][col] == "#":
                rocks[(row, col)] = "#"
    return total


def cycle(crf, sr, r_count, c_count):
    cr = copy.copy(crf)
    # north
    changing = True
    while changing:
        changing = False
        for rock in cr:
            r = rock[0]
            while r > 0 and (r - 1, rock[1]) not in sr and (r - 1, rock[1]) not in cr:
                changing = True
                r -= 1
            cr.remove(rock)
            cr.add((r, rock[1]))

    # west
    changing = True
    while changing:
        changing = False
        for rock in cr:
            c = rock[1]
            while c > 0 and (rock[0], c - 1) not in sr and (rock[0], c - 1) not in cr:
                changing = True
                c -= 1
            cr.remove(rock)
            cr.add((rock[0], c))

    # south
    changing = True
    while changing:
        changing = False
        for rock in cr:
            r = rock[0]
            while r < r_count - 1 and (r + 1, rock[1]) not in sr and (r + 1, rock[1]) not in cr:
                changing = True
                r += 1
            cr.remove(rock)
            cr.add((r, rock[1]))

    # east
    changing = True
    while changing:
        changing = False
        for rock in cr:
            c = rock[1]
            while c < c_count - 1 and (rock[0], c + 1) not in sr and (rock[0], c + 1) not in cr:
                changing = True
                c += 1
            cr.remove(rock)
            cr.add((rock[0], c))
    return cr


def calculate_load(rocks, r_count):
    total = 0
    for rock in rocks:
        total += r_count - rock[0]
    return total


def p2(values):
    circle_rocks = set()
    square_rocks = set()
    for row in range(len(values)):
        for col in range(len(values[row])):
            if values[row][col] == "O":
                circle_rocks.add((row, col))
            elif values[row][col] == "#":
                square_rocks.add((row, col))
    r_count = len(values)
    c_count = len(values[0])
    previous_results = []
    start, length = 0, 0
    for i in range(BILLION):
        circle_rocks = cycle(circle_rocks, square_rocks, r_count, c_count)
        if circle_rocks in previous_results:
            start = previous_results.index(circle_rocks)
            length = i - start
            break
        previous_results.append(circle_rocks)

    print(BILLION, start, length)
    at = start + ((BILLION - 1) - start) % length

    return calculate_load(previous_results[at], r_count)


def main():
    values = read_in()
    # print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
