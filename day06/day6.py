import math


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip().split(":")[1].split() for line in input_file]
    return lines


def distance_gone(held, duration):
    return (duration - held) * held


def p1(values):
    ways_product = 1
    for race in range(len(values[0])):
        ways = 0
        for hold in range(int(values[0][race])):
            if distance_gone(hold, int(values[0][race])) > int(values[1][race]):
                ways += 1
        ways_product *= ways
    return ways_product


def search_start(time, record, start, end):
    mp = start + (end - start) // 2
    if distance_gone(time, mp) > record:
        if distance_gone(time, mp - 1) <= record:
            return mp
        return search_start(time, record, start, mp)
    else:  # distance <= record
        if distance_gone(time, mp + 1) > record:
            return mp
        return search_start(time, record, mp, end)


def p2(values):
    [time, distance] = [int("".join(r)) for r in values]
    D = time  # length of race
    R = distance  # record
    t_1 = (D + math.sqrt(D**2 - (4 * R))) / (-2)
    if -2 * t_1 - D == 0:  # if t_1 is a turning point, there are no solutions
        return 0
    t_2 = (D - math.sqrt(D**2 - (4 * R))) / (-2)
    s = math.floor(min(t_1, t_2)) + 1
    e = math.ceil(max(t_1, t_2))
    return e - s


def main():
    values = read_in()
    print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
