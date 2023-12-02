import math


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip().split(":")[1][1:].split(";") for line in input_file]
    return lines


def check_game(game, max_cubes):
    for game_set in game:
        for colour in game_set.split(","):
            parts = colour.split()
            if int(parts[0]) > max_cubes[parts[1]]:
                return False
    return True


def p1(games):
    total_sum = 0
    max_cubes = {"green": 13, "red": 12, "blue": 14}
    for g in range(len(games)):
        game = games[g]
        if check_game(game, max_cubes):
            total_sum += g + 1

    return total_sum


def p2(games):
    total_sum = 0
    for game in games:
        max_for_game = {"green": 0, "red": 0, "blue": 0}
        for game_set in game:
            for colour in game_set.split(","):
                parts = colour.split()
                max_for_game[parts[1]] = max(int(parts[0]), max_for_game[parts[1]])
        total_sum += math.prod(max_for_game.values())
    return total_sum


def main():
    values = read_in()
    print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
