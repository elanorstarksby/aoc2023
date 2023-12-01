import re


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def calculate_total(line, part):
    # print(line)
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    first = [len(line), 0]
    last = [-1, 0]
    for digit_i in range(1, 10):
        # word digits
        if part == 2:
            digit = digits[digit_i - 1]
            locations_letters = [m.start() for m in re.finditer(re.escape(str(digit)), line)]
            # print(locations)
            if locations_letters:
                if min(locations_letters) < first[0]:
                    first[0] = min(locations_letters)
                    first[1] = digit_i
                if max(locations_letters) > last[0]:
                    last[0] = max(locations_letters)
                    last[1] = digit_i

        # number digits
        locations_numbers = [m.start() for m in re.finditer(re.escape(str(digit_i)), line)]
        if locations_numbers:
            if min(locations_numbers) < first[0]:
                first[0] = min(locations_numbers)
                first[1] = digit_i
            if max(locations_numbers) > last[0]:
                last[0] = max(locations_numbers)
                last[1] = digit_i

    # print(first_digit_value, last_digit_value)

    # print(first_digit_value, last_digit_value)
    # print(10 * first_digit_value + last_digit_value)
    return 10 * first[1] + last[1]


def p1(values):
    p1_total = 0
    for value in values:
        p1_total += calculate_total(value, 1)
    return p1_total


def p2(values):
    p2_total = 0
    for value in values:
        p2_total += calculate_total(value, 2)
    return p2_total


def main():
    values = read_in()
    # print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
