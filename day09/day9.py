from functools import reduce


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [[int(v) for v in l] for l in [line.strip().split() for line in input_file]]
    return lines


def p1(values):
    def all_zero(a):
        for v in a:
            if v != 0:
                return False
        return True

    final_values = []
    for history in values:
        last_sequence = history
        while not all_zero(last_sequence):
            final_values.append(last_sequence[-1])
            last_sequence = [last_sequence[i + 1] - last_sequence[i] for i in range(len(last_sequence) - 1)]

    return sum(final_values)


def p2(values):
    total = 0

    def all_zero(a):
        for v in a:
            if v != 0:
                return False
        return True

    for history in values:
        final_values = []
        last_sequence = history
        while not all_zero(last_sequence):
            final_values.append(last_sequence[0])
            last_sequence = [last_sequence[i + 1] - last_sequence[i] for i in range(len(last_sequence) - 1)]
        last = 0
        for i in range(len(final_values) - 1, -1, -1):
            last = final_values[i] - last
        total += last
    return total


def main():
    values = read_in()
    print(values)
    # print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
