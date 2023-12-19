def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip().split(",") for line in input_file][0]
    return lines


def hash_char(ch, val):
    val += ord(ch)
    val *= 17
    val %= 256
    return val


def hash_string(st):
    # print(st)
    total = 0
    for ch in st:
        total = hash_char(ch, total)
    return total


def p1(values):
    total = 0
    for st in values:
        total += hash_string(st)
    return total


def p2(values):
    boxes = [[] for _ in range(256)]
    map_labels = {}
    for step in values:
        if "=" in step:
            [label, length] = step.split("=")
            box = hash_string(label)
            if label not in boxes[box]:
                boxes[box].append(label)
            # else just replace with same label, different length
            map_labels[label] = int(length)
        else:
            label = step[:-1]
            box = hash_string(label)
            if label in boxes[box]:
                boxes[box].remove(label)
    total = 0
    for b in range(256):
        for le in range(len(boxes[b])):
            length = map_labels[boxes[b][le]]
            total += (b + 1) * (le + 1) * length

    return total


def main():
    values = read_in()
    # print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
