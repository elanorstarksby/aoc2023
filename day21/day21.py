import datetime


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def find_start(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "S":
                return r, c


DEPTH = 64


def search(grid, loc, depth, visited, max_rc, exp):
    # print(depth)
    if loc in exp:
        return visited, exp

    visited.add(loc)

    if depth == DEPTH:
        return visited, exp

    if loc[0] + 1 < max_rc[0] and grid[loc[0] + 1][loc[1]] == ".":
        visited, exp = search(grid, (loc[0] + 1, loc[1]), depth + 1, visited, max_rc, exp)
    if 0 <= loc[0] - 1 and grid[loc[0] - 1][loc[1]] == ".":
        visited, exp = search(grid, (loc[0] - 1, loc[1]), depth + 1, visited, max_rc, exp)
    if loc[1] + 1 < max_rc[1] and grid[loc[0]][loc[1] + 1] == ".":
        visited, exp = search(grid, (loc[0], loc[1] + 1), depth + 1, visited, max_rc, exp)
    if 0 <= loc[1] - 1 and grid[loc[0]][loc[1] - 1] == ".":
        visited, exp = search(grid, (loc[0], loc[1] - 1), depth + 1, visited, max_rc, exp)

    exp.add(loc)

    return visited, exp


def search2(grid, start):
    height = len(grid)
    width = len(grid[0])
    even = set()
    explore_next = {start}
    for i in range(DEPTH + 1):
        explore_now = explore_next
        explore_next = set()
        for point in explore_now:
            if 0 <= point[0] < height and 0 <= point[1] < width and grid[point[0]][point[1]] != "#":
                if i % 2 == 0:
                    even.add(point)
                explore_next.add((point[0] + 1, point[1]))
                explore_next.add((point[0] - 1, point[1]))
                explore_next.add((point[0], point[1] + 1))
                explore_next.add((point[0], point[1] - 1))
    return even


def p1(grid):
    # dfs
    # any . reached in even number of steps <=64 can be reached in 64
    start = find_start(grid)
    # max_rc = (len(grid), len(grid[0]))
    # visited, e = search(grid, start, 0, set(), max_rc, set())
    # print(visited)
    # visited = {(x[0], x[1]): 0 for x in filter(lambda x: (((x[0] - start[0]) + (x[1] - start[1])) % 2 == 0), visited)}
    # print(visited)
    # for r in range(max_rc[0]):
    #     print("".join([str(visited[(r, x)]) if (r, x) in visited and visited[(r, x)] % 2 == 0 else "#" if grid[r][
    #                                                                                                           x] == "#" else "."
    #                    for x in range(max_rc[1])]))
    # return len(list(filter(lambda x: x[1] % 2 == 0, visited.items())))
    visited = search2(grid, start)

    # for r in range(len(grid)):
    #     print("".join(["O" if (r, x) in visited else "#" if grid[r][x] == "#" else "." for x in range(len(grid[0]))]))
    return len(visited)


def p2(values):
    return 0


def main():
    values = read_in()
    # print(values)
    t = datetime.datetime.now()
    print(p1(values))
    print((datetime.datetime.now() - t))
    print(p2(values))


if __name__ == '__main__':
    main()
