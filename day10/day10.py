def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def find_start(values):
    for r in range(len(values)):
        row = values[r]
        try:
            c = row.index("S")
            return r, c
        except ValueError:
            pass
    return -1, -1


north, east, south, west = (0, -1), (1, 0), (0, 1), (-1, 0)
pipes = {"|": (north, south), "-": (east, west), "7": (west, south), "J": (north, west), "F": (south, east),
         "L": (north, east)}


def move(cr, cc, enter, value):
    choices = pipes[value]
    # can't go back the way entered
    no = tuple(-d for d in enter)
    # print(choices, enter, no)
    direction = choices[0] if choices[0] != no else choices[1]
    return cr + direction[1], cc + direction[0], direction


def p1(values, start_replace):
    sr, sc = find_start(values)
    # print(sr, sc)
    # values[sr] = values[sr].replace("S", start_replace)
    enter = pipes[start_replace][0]  # choose one of the directions to start
    cr, cc, enter = move(sr, sc, enter, start_replace)
    # print("move", enter)
    moves = 1
    current_pipe = values[cr][cc]
    visited = {(sr, sc)}
    while current_pipe != "S":
        # print("move", enter)
        visited.add((cr, cc))
        cr, cc, enter = move(cr, cc, enter, current_pipe)
        current_pipe = values[cr][cc]
        moves += 1
    return moves // 2, visited


def double_width(grid, visited):
    new_grid = [['.' for _ in range(2 * len(item))] for item in grid]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (row, col) not in visited:  # ignore pipes that aren't in loop
                continue
            p = grid[row][col]
            new_grid[row][2 * col] = p
            if p in ["F", "-", "L"]:
                new_grid[row][2 * col + 1] = "-"
    for g in new_grid:
        g.pop()
    return new_grid


def double_height(grid, visited):
    new_grid = [['.' for _ in range(len(item))] for item in grid for _ in range(2)]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (row, col//2) not in visited:
                continue
            p = grid[row][col]
            new_grid[2 * row][col] = p
            if p in ["F", "|", "7"]:
                new_grid[2 * row + 1][col] = "|"
    return new_grid[:-1]


def p2(values, start_replace):
    _, visited = p1(values, start_replace)
    sr, sc = find_start(values)
    values[sr] = values[sr].replace("S", start_replace)

    w_doubled_grid = double_width(values, visited)
    hw_doubled_grid = double_height(w_doubled_grid, visited)

    hw_doubled_grid[0] = ["O" if i == "." else i for i in hw_doubled_grid[0]]
    hw_doubled_grid[-1] = ["O" if i == "." else i for i in hw_doubled_grid[-1]]

    for r in range(len(hw_doubled_grid)):
        if hw_doubled_grid[r][0] == ".":
            hw_doubled_grid[r][0] = "O"
        if hw_doubled_grid[r][-1] == ".":
            hw_doubled_grid[r][-1] = "O"

    changed = True
    while changed:
        changed = False
        for r in range(len(hw_doubled_grid)):
            for c in range(len(hw_doubled_grid[r])):
                if hw_doubled_grid[r][c] == "O":
                    for direction in (north, south, east, west):
                        try:
                            if hw_doubled_grid[r+direction[0]][c+direction[1]] == ".":
                                changed = True
                                hw_doubled_grid[r+direction[0]][c+direction[1]] = "O"
                        except IndexError:
                            pass
    # for r in grid:
    #     print("".join(r))

    count = 0
    for r in range(len(values)):
        for c in range(len(values[r])):
            if (r, c) not in visited:
                if hw_doubled_grid[r*2][c*2] == ".":
                    count += 1
                    hw_doubled_grid[r*2][c*2] = "I"
                    row = [a for a in values[r]]
                    row[c] = "I"
                    values[r] = "".join(row)
    # for r in values:
    #     print(r)
    return count


def main():
    values = read_in()
    start_replace = "7"
    print(p1(values, start_replace)[0])

    print(p2(values, start_replace))


if __name__ == '__main__':
    main()
