import networkx as nx


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def p1(values):
    graph = nx.Graph()
    # edges = set()
    for il in values:
        s, others = il.split(":")
        for o in others.split():
            # edges.add((min(s, o), max(s, o)))
            graph.add_edge(o, s)
    count, cut = nx.stoer_wagner(graph)

    # print(edges)
    print(count, cut)
    return len(cut[0]) * len(cut[1])


def p2(values):
    return 0


def main():
    values = read_in()
    # print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
