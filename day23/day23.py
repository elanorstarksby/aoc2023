import datetime


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def p1(values: list[str]):
    start = (0, values[0].index("."))
    end = (len(values) - 1, values[len(values) - 1].index("."))
    print(end)
    explore = {(start,)}
    paths = set()
    while explore:
        path = explore.pop()
        (cr, cc) = path[-1]
        if (cr, cc) == end:
            paths.add(path)
            continue
        if cr < len(values) - 1 \
                and values[cr][cc] in [".", "v"] and values[cr + 1][cc] in [".", "v"] \
                and (cr + 1, cc) not in path:
            explore.add(path + ((cr + 1, cc),))
        if cr > 0 \
                and values[cr][cc] in [".", "^"] \
                and values[cr - 1][cc] in [".", "^"] \
                and (cr - 1, cc) not in path:
            explore.add(path + ((cr - 1, cc),))
        if cc < len(values[0]) - 1 \
                and values[cr][cc] in [".", ">"] \
                and values[cr][cc + 1] in [".", ">"] \
                and (cr, cc + 1) not in path:
            explore.add(path + ((cr, cc + 1),))
        if cc > 0 \
                and values[cr][cc] in [".", "<"] \
                and values[cr][cc - 1] in [".", "<"] \
                and (cr, cc - 1) not in path:
            explore.add(path + ((cr, cc - 1),))
    return max(map(lambda x: len(x) - 1, paths))


def p2(values: list[str]):
    start = (0, values[0].index("."))
    end = (len(values) - 1, values[len(values) - 1].index("."))
    print(end)
    explore = {(start,)}
    paths = set()
    while explore:
        path = explore.pop()
        (cr, cc) = path[-1]
        if (cr, cc) == end:
            paths.add(path)
            continue
        if cr < len(values) - 1 \
                and values[cr + 1][cc] != "#" \
                and (cr + 1, cc) not in path:
            explore.add(path + ((cr + 1, cc),))
        if cr > 0 \
                and values[cr - 1][cc] != "#" \
                and (cr - 1, cc) not in path:
            explore.add(path + ((cr - 1, cc),))
        if cc < len(values[0]) - 1 \
                and values[cr][cc + 1] != "#" \
                and (cr, cc + 1) not in path:
            explore.add(path + ((cr, cc + 1),))
        if cc > 0 \
                and values[cr][cc - 1] != "#" \
                and (cr, cc - 1) not in path:
            explore.add(path + ((cr, cc - 1),))
    return max(map(lambda x: len(x) - 1, paths))


def main():
    values = read_in()
    print(values)
    t1 = datetime.datetime.now()
    print(p1(values))
    t2 = datetime.datetime.now()
    print(t2 - t1)
    print(p2(values))
    print(datetime.datetime.now() - t2)


if __name__ == '__main__':
    main()
