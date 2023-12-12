import itertools

SIZE = 1000000


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def p1(values):
    r = 0
    while r < len(values):
        if values[r] == "".join(["." for _ in range(len(values[r]))]):
            values.insert(r, "".join(["." for _ in range(len(values[r]))]))
            r += 1
        r += 1
    cols_to_add = []
    for c in range(len(values[0])):
        add = True
        for r in range(len(values)):
            if values[r][c] != ".":
                add = False
        if add:
            cols_to_add.append(c + len(cols_to_add))

    for r in range(len(values)):
        for c in cols_to_add:
            values[r] = values[r][:c] + "." + values[r][c:]

    # for row in values:
    #     print(row)

    galaxy_locations = set()
    for r in range(len(values)):
        for c in range(len(values[r])):
            if values[r][c] == "#":
                galaxy_locations.add((r, c))

    pairs = list(itertools.combinations(galaxy_locations, 2))
    # print(len(pairs))
    total = 0
    for galaxy_pair in pairs:
        # print(galaxy_pair, d)
        total += abs(galaxy_pair[0][0] - galaxy_pair[1][0]) + abs(galaxy_pair[0][1] - galaxy_pair[1][1])

    return total


def p2(values):
    rows_to_add = []
    for r in range(len(values)):
        if values[r] == "".join(["." for _ in range(len(values[r]))]):
            rows_to_add.append(r)

    cols_to_add = []
    for c in range(len(values[0])):
        add = True
        for r in range(len(values)):
            if values[r][c] != ".":
                add = False
        if add:
            cols_to_add.append(c)

    galaxy_locations = set()
    for r in range(len(values)):
        for c in range(len(values[r])):
            if values[r][c] == "#":
                galaxy_locations.add((r, c))

    pairs = list(itertools.combinations(galaxy_locations, 2))
    # print(len(pairs))
    total = 0
    for galaxy_pair in pairs:
        # print(galaxy_pair, d)
        ((y1, x1), (y2, x2)) = galaxy_pair
        d = abs(y1 - y2) + abs(x1 - x2)
        total += d
        # print(galaxy_pair)
        for v_line in cols_to_add:
            if x1 < v_line < x2 or x2 < v_line < x1:
                # print("v", v_line)
                total += SIZE - 1
        for h_line in rows_to_add:
            if y1 < h_line < y2 or y2 < h_line < y1:
                # print("h", h_line)
                total += SIZE - 1
        # print(d)

    return total


def main():
    values = read_in()
    # print(values)
    print(p1(values.copy()))

    print(p2(values))


if __name__ == '__main__':
    main()
