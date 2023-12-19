def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip().split() for line in input_file]
    return lines


def find_area(corners: list):
    area = 0

    for i in range(len(corners)):
        j = (i + 1) % len(corners)

        area += corners[i][1] * corners[j][0]
        area -= corners[i][0] * corners[j][1]

    area /= 2
    return abs(area)


def p1(values):
    directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    dug = 0
    pos = (0, 0)
    corners = [pos]
    for step in values:
        pos = tuple(pos[c] + int(step[1]) * directions[step[0]][c] for c in range(2))
        dug += int(step[1])
        corners.append(pos)

    return find_area(corners) + dug / 2 + 1


def extract(code):
    distance_encoded = code[2:7]
    direction_encoded = int(code[-2])
    return "RDLU"[direction_encoded], int(distance_encoded, 16)


def p2(values):
    steps = []
    for step in values:
        steps.append(extract(step[2]))
    return p1(steps)


def main():
    values = read_in()
    print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
