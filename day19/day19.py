class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        self.map_strings = {"x": x, "m": m, "a": a, "s": s}

    def get(self, value_string):
        return self.map_strings[value_string]

    def combinations(self):
        return (self.x[1] - self.x[0]) * (self.m[1] - self.m[0]) * (self.a[1] - self.a[0]) * (self.s[1] - self.s[0])


class Step:
    def __init__(self, step_string: str):
        if len(step_string.split(":")) == 1:
            self.dest_only = True
            self.destination = step_string
            return
        self.dest_only = False
        [com, self.destination] = step_string.split(":")
        self.xmas: str = com[0]
        self.gt: bool = com[1] == ">"
        self.comparator: int = int(com[2:])

    def eval(self, part: Part):
        if self.dest_only:
            return True
        if self.gt:
            return part.get(self.xmas) > self.comparator
        else:
            return part.get(self.xmas) < self.comparator

    def split(self, part: Part):
        split_at = self.comparator + 1 if self.gt else self.comparator

        if self.xmas == "x":
            return Part((part.x[0], split_at), part.m, part.a, part.s), \
                Part((split_at, part.x[1]), part.m, part.a, part.s)

        if self.xmas == "m":
            return Part(part.x, (part.m[0], split_at), part.a, part.s), \
                Part(part.x, (split_at, part.m[1]), part.a, part.s)

        if self.xmas == "a":
            return Part(part.x, part.m, (part.a[0], split_at), part.s), \
                Part(part.x, part.m, (split_at, part.a[1]), part.s)

        if self.xmas == "s":
            return Part(part.x, part.m, part.a, (part.s[0], split_at)), \
                Part(part.x, part.m, part.a, (split_at, part.s[1]))

    def get_rule_string(self):
        if self.dest_only:
            return self.destination
        return "{0}{1}{2}: {3}".format(self.xmas, ">" if self.gt else "<", self.comparator, self.destination)


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    workflows = {}
    l = 0
    while lines[l] != '':
        name, line = lines[l].split("{")
        steps = []
        for step in line[:-1].split(","):
            steps.append(Step(step))
        workflows[name] = steps
        l += 1
    parts = []
    for line in lines[l + 1:]:
        [x, m, a, s] = [int(v.split("=")[1]) for v in line[1:-1].split(",")]
        parts.append(Part(x, m, a, s))
    return workflows, parts


def next_wf(part: Part, workflow: list[Step]):
    i = 0
    while True:
        current_step = workflow[i]
        if current_step.eval(part):
            return current_step.destination
        i += 1


def p1(workflows, parts):
    accepted_total = 0
    for part in parts:
        wf = "in"
        while wf != "R" and wf != "A":
            wf = next_wf(part, workflows[wf])
        if wf == "A":
            accepted_total += sum(part.map_strings.values())
    return accepted_total


def p2(workflows: {str: list[Step]}, max_inc):
    combinations = 0
    queue = [(Part((1, max_inc + 1), (1, max_inc + 1), (1, max_inc + 1), (1, max_inc + 1)), "in", 0)]
    while queue:
        part, wf, step_n = queue.pop()
        if wf != "R" and wf != "A":
            step: Step = workflows[wf][step_n]
            if step.dest_only:
                queue.append((part, step.destination, 0))
                continue

            lower, upper = step.split(part)
            if step.gt:
                queue.append((upper, step.destination, 0))
                queue.append((lower, wf, step_n + 1))
            else:
                queue.append((lower, step.destination, 0))
                queue.append((upper, wf, step_n + 1))
        elif wf == "A":
            combinations += part.combinations()
    return combinations


def main():
    workflows, parts = read_in()
    print(p1(workflows, parts))
    print(p2(workflows, 4000))


if __name__ == '__main__':
    main()
