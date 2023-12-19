from collections import namedtuple

Beam = namedtuple('Beam', ['r', 'c', 'dr', 'dc'])


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def energize(start: Beam, values):
    row_count = len(values)
    col_count = len(values[0])
    reflect_forwards = {(0, 1): (-1, 0), (0, -1): (1, 0), (1, 0): (0, -1), (-1, 0): (0, 1)}
    reflect_backward = {(0, 1): (1, 0), (0, -1): (-1, 0), (1, 0): (0, 1), (-1, 0): (0, -1)}

    queue = [start]
    pos_visited = set()
    beams_visited = set()
    while queue:
        r, c, dr, dc = queue.pop()
        while (r, c, dr, dc) not in beams_visited:
            pos_visited.add((r, c))
            beams_visited.add((r, c, dr, dc))

            tile = values[r][c]
            if tile == "." or (tile == "|" and dc == 0) or (tile == "-" and dr == 0):
                pass
            elif tile == "|":
                if r > 0:
                    queue.append(Beam(r - 1, c, -1, 0))
                dr, dc = 1, 0
            elif tile == "-":
                if c > 0:
                    queue.append(Beam(r, c - 1, 0, -1))
                dr, dc = 0, 1
            elif tile == "/":
                dr, dc = reflect_forwards[(dr, dc)]
            elif tile == "\\":
                dr, dc = reflect_backward[(dr, dc)]

            r += dr
            c += dc
            if r < 0 or r >= row_count or c < 0 or c >= col_count:
                break

    # print(pos_visited)
    # for row in range(row_count):
    #     print("".join("#" if (row, c) in pos_visited else "." for c in range(col_count)))
    return len(pos_visited)


def p1(values):
    return energize(Beam(0, 0, 0, 1), values)


def p2(values):
    row_count = len(values)
    col_count = len(values[0])

    current_max = 0
    for row in range(row_count):
        current_max = max(current_max, energize(Beam(row, 0, 0, 1), values))
        current_max = max(current_max, energize(Beam(row, col_count - 1, 0, -1), values))
    for col in range(col_count):
        current_max = max(current_max, energize(Beam(0, col, 1, 0), values))
        current_max = max(current_max, energize(Beam(row_count-1, col - 1, -1, 0), values))
    return current_max


def main():
    values = read_in()
    print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
