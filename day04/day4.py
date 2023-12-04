from functools import reduce


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip().split(":")[1].split("|") for line in input_file]
    return lines


def score_card(card):
    winning = [int(v) for v in card[0].split()]
    have = [int(v) for v in card[1].split()]
    matches = 0
    for number in have:
        if number in winning:
            matches += 1
    if matches > 0:
        return matches, 2 ** (matches - 1)
    return matches, 0


def p1(cards):
    points = 0
    for card in cards:
        points += score_card(card)[1]
    return points


def copy_cards(scores):
    total = 0
    for card_number in range(len(scores)):
        matches = scores[card_number][0]
        for i in range(matches):
            # print(i)
            scores[card_number + i + 1][1] += scores[card_number][1]
    for card in scores:
        total += card[1]
    return total


def p2(values):
    scores = []
    for card in values:
        scores.append([score_card(card)[0], 1])
    return copy_cards(scores)


def main():
    values = read_in()
    # print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
