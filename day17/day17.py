import heapq


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def p1(values):
    start = (0, 0)

    target = (len(values) - 1, len(values[0]) - 1)
    #        dist  pos    dir   times
    queue = [(0, start, (0, 0), 0)]
    visited = set()
    while True:
        dist, pos, direction, times_direction = heapq.heappop(queue)
        if pos == target:
            return dist
        if (pos, direction, times_direction) in visited:
            continue
        visited.add((pos, direction, times_direction))
        for next_direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_pos = (pos[0] + next_direction[0], pos[1] + next_direction[1])
            next_times = times_direction + 1 if direction == next_direction else 1
            if not 0 <= next_pos[0] <= len(values) - 1:  # outside grid
                continue
            if not 0 <= next_pos[1] <= len(values[0]) - 1:  # outside grid
                continue
            if (next_pos, next_direction, next_times) in visited:
                continue
            if times_direction == 3 and next_direction == direction:
                continue
            if (-direction[0], -direction[1]) == next_direction:
                continue
            heapq.heappush(queue, (
                dist + int(values[next_pos[0]][next_pos[1]]),
                next_pos,
                next_direction,
                next_times
            ))


def p2(values):
    start = (0, 0)

    target = (len(values) - 1, len(values[0]) - 1)
    #        dist  pos    dir   times
    queue = [(0, start, (0, 1), 0), (0, start, (1, 0), 0)]
    heapq.heapify(queue)
    visited = set()
    while True:
        dist, pos, direction, times_direction = heapq.heappop(queue)
        if pos == target and times_direction >= 4:
            return dist
        if (pos, direction, times_direction) in visited:
            continue
        visited.add((pos, direction, times_direction))
        for next_direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if times_direction < 4 and next_direction != direction:
                continue
            next_pos = (pos[0] + next_direction[0], pos[1] + next_direction[1])
            next_times = times_direction + 1 if direction == next_direction else 1
            if not 0 <= next_pos[0] <= len(values) - 1:  # outside grid
                continue
            if not 0 <= next_pos[1] <= len(values[0]) - 1:  # outside grid
                continue
            if (next_pos, next_direction, next_times) in visited:
                continue
            if times_direction == 10 and next_direction == direction:
                continue
            if (-direction[0], -direction[1]) == next_direction:
                continue
            heapq.heappush(queue, (
                dist + int(values[next_pos[0]][next_pos[1]]),
                next_pos,
                next_direction,
                next_times
            ))


def main():
    values = read_in()
    print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
