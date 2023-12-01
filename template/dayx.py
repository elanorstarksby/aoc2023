def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def p1(values):
    return 0


def p2(values):
    return 0


def main():
    values = read_in()
    # print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
