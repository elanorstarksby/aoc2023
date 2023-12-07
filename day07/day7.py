def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip().split() for line in input_file]
    return lines


def hand_type(hand):
    cards_count = {}
    for hc in hand:
        if hc not in cards_count:
            cards_count[hc] = 0
        cards_count[hc] = cards_count[hc] + 1
    # five of a kind
    if len(cards_count.keys()) == 1:
        return 6
    # four of a kind
    if len(cards_count.keys()) == 2 and cards_count.get(max(cards_count, key=cards_count.get)) == 4:
        return 5
    # full house
    if len(cards_count.keys()) == 2 and cards_count.get(max(cards_count, key=cards_count.get)) == 3:
        return 4
    # three of a kind
    if len(cards_count.keys()) == 3 and cards_count.get(max(cards_count, key=cards_count.get)) == 3:
        return 3
    # two pair
    if len(cards_count.keys()) == 3 and cards_count.get(max(cards_count, key=cards_count.get)) == 2:
        return 2
    # one pair
    if len(cards_count.keys()) == 4 and cards_count.get(max(cards_count, key=cards_count.get)) == 2:
        return 1
    # high card
    if len(cards_count.keys()) == 5:
        return 0
    raise Exception("Card has no type")


def p1(values):
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    for hand in values:
        hand.append(hand_type(hand[0]))
    s = sorted(values, key=lambda x: (
        x[2], -cards.index(x[0][0]), -cards.index(x[0][1]), -cards.index(x[0][2]), -cards.index(x[0][3]),
        -cards.index(x[0][4])))

    total = 0
    for i in range(len(s)):
        total += (i + 1) * int(s[i][1])
    return total


def is_five(cards_count):
    return len(cards_count.keys()) == 1 or (len(cards_count.keys()) == 2 and 'J' in cards_count)


def is_four(cards_count):  # is at least 4
    return (len(cards_count.keys()) == 2 and cards_count.get(max(cards_count, key=cards_count.get)) == 4) or (
            len(cards_count.keys()) == 3 and 'J' in cards_count and (cards_count.get(
        max(cards_count, key=cards_count.get)) == 3 or cards_count['J'] == 2))


def is_full(cards_count):  # full house after ruling out 4+
    return (len(cards_count.keys()) == 2 and cards_count.get(max(cards_count, key=cards_count.get)) == 3) or (
            len(cards_count) == 3 and 'J' in cards_count)


def is_three(cards_count):
    return (len(cards_count.keys()) == 3 and cards_count.get(max(cards_count, key=cards_count.get)) == 3) or (
            len(cards_count.keys()) == 4 and 'J' in cards_count and cards_count.get(
        max(cards_count, key=cards_count.get)) == 2)


def is_two_pair(cards_count):
    return len(cards_count.keys()) == 3 and cards_count.get(max(cards_count, key=cards_count.get)) == 2


def is_one_pair(cards_count):
    return (len(cards_count.keys()) == 4 and cards_count.get(max(cards_count, key=cards_count.get)) == 2) or (
            len(cards_count.keys()) == 5 and 'J' in cards_count)


def hand_type_p2(hand):
    cards_count = {}
    for hc in hand:
        if hc not in cards_count:
            cards_count[hc] = 0
        cards_count[hc] = cards_count[hc] + 1
    # print(cards_count)
    # five of a kind
    if is_five(cards_count):
        return 6
    # four of a kind
    if is_four(cards_count):
        return 5
    # full house
    if is_full(cards_count):
        return 4
    # three of a kind
    if is_three(cards_count):
        return 3
    # two pair
    if is_two_pair(cards_count):
        return 2
    # one pair
    if is_one_pair(cards_count):
        return 1
    # high card
    if len(cards_count.keys()) == 5:
        return 0
    raise Exception("Card has no type")


def p2(values):
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    for hand in values:
        hand[2] = (hand_type_p2(hand[0]))
    print(values)
    s = sorted(values, key=lambda x: (
        x[2], -cards.index(x[0][0]), -cards.index(x[0][1]), -cards.index(x[0][2]), -cards.index(x[0][3]),
        -cards.index(x[0][4])))

    total = 0
    for i in range(len(s)):
        total += (i + 1) * int(s[i][1])
    return total


def main():
    values = read_in()
    print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
