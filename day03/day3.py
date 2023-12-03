import re


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line for line in input_file]
    return lines


def search_around(span, line, grid, regex):
    start = span[0]
    end = span[1]
    grid = [l.strip() for l in grid]
    # before number starts
    if start > 0 and line > 0:
        if re.match(regex, grid[line - 1][start - 1]):
            return True, (line - 1, start - 1)
    if start > 0:
        if re.match(regex, grid[line][start - 1]):
            return True, (line, start - 1)
    if start > 0 and line < len(grid) - 1:
        if re.match(regex, grid[line + 1][start - 1]):
            return True, (line + 1, start - 1)
    # above number
    if line > 0:
        for i in range(start, end):
            if re.match(regex, grid[line - 1][i]):
                return True, (line - 1, i)
    # below number
    if line < len(grid) - 1:
        for i in range(start, end):
            if re.match(regex, grid[line + 1][i]):
                return True, (line + 1, i)
    # after number ends
    if end < len(grid[line]) and line > 0:
        if re.match(regex, grid[line - 1][end]):
            return True, (line - 1, end)
    if end < len(grid[line]):
        if re.match(regex, grid[line][end]):
            return True, (line, end)
    if end < len(grid[line]) and line < len(grid) - 1:
        if re.match(regex, grid[line + 1][end]):
            return True, (line + 1, end)
    return False, ()


def p1(values):
    total = 0
    for line in range(len(values)):
        numbers = re.finditer('[0-9]+', values[line])
        for each in numbers:
            span = each.span()
            if search_around(span, line, values, '[^0-9.]')[0]:
                # print(each)
                total += int(each.group(0))
    return total


def p2(values):
    symbols = {}
    for line in range(len(values)):
        numbers = re.finditer('[0-9]+', values[line])
        for each in numbers:
            span = each.span()
            found, location = search_around(span, line, values, '\\*')
            if found and values[location[0]][location[1]] == "*":
                # print(each)
                if location not in symbols:
                    symbols[location] = []
                symbols[location].append(int(each.group(0)))
    total = 0
    for symbol in symbols:
        if len(symbols[symbol]) == 2:
            total += symbols[symbol][0] * symbols[symbol][1]

    return total


def main():
    values = read_in()
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
