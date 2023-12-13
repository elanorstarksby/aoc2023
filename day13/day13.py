def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def reflect_horizontal(pattern, row):
    # print()
    row_count = min(len(pattern) - row - 1, row + 1)
    for rc in range(row_count):
        before = row - rc
        after = row + rc + 1
        # print(pattern[before], pattern[after])
        if pattern[before] != pattern[after]:
            return False
    # print("row", row)
    return True


def reflect_vertical(pattern, col):
    # print()
    col_count = min(len(pattern[0]) - col - 1, col + 1)
    for cc in range(col_count):
        before = col - cc
        after = col + cc + 1
        pb = [r[before] for r in pattern]
        pa = [r[after] for r in pattern]
        # print(pb, pa)
        if pb != pa:
            return False
    # print("col", col)
    return True


def p1(values):
    originals = []
    i = 0
    total = 0
    while i < len(values):
        # print()
        pattern = []
        while i < len(values) and values[i] != '':
            pattern.append(values[i])
            i += 1
        # print(pattern)
        i += 1
        done = False
        for r in range(0, len(pattern) - 1):
            if reflect_horizontal(pattern, r):
                total += 100 * (r+1)
                originals.append(("row", r))
                done = True
                break
        if not done:
            for c in range(0, len(pattern[0]) - 1):
                if reflect_vertical(pattern, c):
                    total += c + 1
                    originals.append(("col", c))
                    done = True
                    break
        # print(done)
    return total, originals


def p2(values):
    _, originals = p1(values)
    i = 0
    pattern_index = -1
    total = 0
    while i < len(values):
        pattern_index += 1
        # print()
        pattern_o = []
        while i < len(values) and values[i] != '':
            pattern_o.append(values[i])
            i += 1
        i += 1
        # print(pattern)
        patterns = []
        for r in range(len(pattern_o)):
            for c in range(len(pattern_o[r])):
                pattern_c = pattern_o.copy()
                ch = pattern_c[r][c]
                rp = "." if ch == "#" else "#"
                pattern_c[r] = pattern_c[r][:c] + rp + pattern_c[r][c+1:]
                patterns.append(pattern_c)

        for pattern in patterns:
            done = False
            for r in range(0, len(pattern) - 1):
                if reflect_horizontal(pattern, r):
                    if originals[pattern_index] != ("row", r):
                        total += 100 * (r+1)
                        done = True
                        break
            if not done:
                for c in range(0, len(pattern[0]) - 1):
                    if reflect_vertical(pattern, c):
                        if originals[pattern_index] != ("col", c):
                            total += c + 1
                            done = True
                            break

            # print(done)
            if done:
                # for p in pattern:
                #     print(p)
                break
    return total


def main():
    values = read_in()
    # print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
