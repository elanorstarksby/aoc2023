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


def p2(values):
    return p1([[int("".join(r))] for r in values])


def main():
    values = read_in()
    print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
