import functools
from itertools import product


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip().split() for line in input_file]

    for i in range(len(lines)):
        l = lines[i]
        lines[i] = ([l[0], [int(n) for n in l[1].split(",")]])
    return lines


def cqm(line):
    return line.count("?")


@functools.cache
def ways_recursive(line, groups, expected):
    if len(line) == 0:  # base case
        if len(groups) == 0:
            return 1
        else:
            return 0

    s = line[0]

    if expected is not None and s != expected and s != "?":  # doesn't work as expecting something else
        return 0

    if s == ".":  # operational
        return ways_recursive(line[1:], groups, None)

    if s == "#":
        if len(groups) == 0:
            return 0
        if groups[0] == 1:
            return ways_recursive(line[1:], groups[1:], ".")
        else:
            return ways_recursive(line[1:], (groups[0] - 1,) + groups[1:], "#")

    if s == "?":
        if expected is not None:
            return ways_recursive(expected + line[1:], groups, None)
        else:
            return ways_recursive("." + line[1:], groups, None) + ways_recursive("#" + line[1:], groups, None)


def count_ways(line, groups):
    arrangements = product((".", "#"), repeat=cqm(line))
    ways = 0
    for a in arrangements:
        this_line = line
        ac = 0
        for c in range(len(this_line)):
            if this_line[c] == "?":
                this_line = this_line[:c] + a[ac] + this_line[c + 1:]
                ac += 1
        this_line_groups = [len(group) for group in this_line.replace(".", " ").split()]
        # print(this_line_groups, this_line_groups == groups)
        if this_line_groups == groups:
            ways += 1
    return ways


def p1(values):
    ways = 0
    for line in values:
        ways += ways_recursive(line[0], tuple(line[1]), None)

    return ways


def p2(values):
    ways = 0
    for line in values:
        ways += ways_recursive(((line[0] + "?") * 5)[:-1], tuple(line[1] * 5), None)

    return ways


def main():
    values = read_in()
    # print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
