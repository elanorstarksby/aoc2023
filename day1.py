import re


def read_in_1d():
    with open("day1.txt", "r") as input_file:
        lines = [[l for l in line.strip()] for line in input_file]
    return lines


def calculate_total(line):
    # print(line)
    digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    first_digit = len(line)
    first_digit_value = 0
    last_digit = -1
    last_digit_value = 0
    # word digits
    for digit in digits.keys():
        locations = [m.start() for m in re.finditer(re.escape(str(digit)), "".join(line))]
        # print(locations)
        if locations:
            if min(locations) < first_digit:
                first_digit = min(locations)
                first_digit_value = digits[digit]
            if max(locations) > last_digit:
                last_digit = max(locations)
                last_digit_value = digits[digit]
    # print(first_digit_value, last_digit_value)

    # number digits
    for i in range(0, 10):
        locations = [m.start() for m in re.finditer(str(i), "".join(line))]
        if locations:
            if min(locations) < first_digit:
                first_digit = min(locations)
                first_digit_value = i
            if max(locations) > last_digit:
                last_digit = max(locations)
                last_digit_value = i
    # print(first_digit_value, last_digit_value)
    # print(10 * first_digit_value + last_digit_value)
    return 10 * first_digit_value + last_digit_value


def main():
    values = read_in_1d()
    # print(values)
    total = 0
    for value in values:
        digits_added = 0
        final = 0
        for c in value:

            try:
                v = int(c)
                if digits_added == 0:
                    # print(10 * v)
                    total += 10 * v
                    final = v
                else:
                    final = v
                digits_added += 1
            except ValueError:
                # print("NO", c)
                pass
        # print(final)
        total += final
    print(total)

    p2_total = 0
    for value in values:
        p2_total += calculate_total(value)
    print(p2_total)


if __name__ == '__main__':
    main()
