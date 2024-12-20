import math
from functools import reduce


class Module:
    modules = {}
    high_count = 0
    low_count = 0
    process_queue = []
    important = {"nx": -1, "sp": -1, "cc": -1, "jq": -1}
    presses = 0

    def __init__(self, name):
        Module.modules[name] = self
        self.destinations = []
        self.last_input = False
        self.name = name

    def add_destination(self, name):
        self.destinations.append(Module.modules[name])

    def add_input(self, name):
        pass

    def receive(self, input_high, from_module):
        if self.name in Module.important and not input_high and Module.important[self.name] < 0:
            Module.important[self.name] = Module.presses
        if input_high:
            Module.high_count += 1
        else:
            Module.low_count += 1
        self.last_input = input_high

    def send(self, send_high):
        for destination in self.destinations:
            Module.process_queue.append((destination, send_high, self))


class FlipFlop(Module):
    def __init__(self, name):
        super().__init__(name)
        self.state = False

    def receive(self, input_high, from_module):
        super().receive(input_high, from_module)
        if not input_high:
            self.state = not self.state
            self.send(self.state)


class Conjunction(Module):
    def __init__(self, name):
        super().__init__(name)
        self.state = {}

    def add_input(self, name):
        self.state[name] = False

    def receive(self, input_high, input_module):
        super().receive(input_high, input_module)
        self.state[input_module.name] = input_high
        self.send(not all(self.state.values()))


class Broadcaster(Module):
    def __init__(self):
        super().__init__("broadcaster")

    def receive(self, input_high, from_module):
        super().receive(input_high, from_module)
        self.send(input_high)


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]

    mapping = {}
    for line in lines:
        [m, d] = line.split(" -> ")
        if m[0] == "%":
            m = m[1:]
            FlipFlop(m)
        elif m[0] == "&":
            m = m[1:]
            Conjunction(m)
        elif m == "broadcaster":
            Broadcaster()
        destinations = d.split(", ")
        mapping[m] = destinations

    for module, destinations in mapping.items():
        for destination in destinations:
            if destination not in Module.modules:
                Module(destination)
            Module.modules[module].add_destination(destination)
            Module.modules[destination].add_input(module)


def p1():
    for i in range(1000):
        Module.modules["broadcaster"].receive(False, None)
        print(Module.process_queue)
        while Module.process_queue:
            module, value, from_module = Module.process_queue.pop(0)
            print(from_module.name + " -" + ("high" if value else "low") + "-> " + module.name)
            module.receive(value, from_module)

    print(Module.high_count, Module.low_count)
    return Module.high_count * Module.low_count


def p2():
    while not all(map(lambda x: x > -1, Module.important.values())):
        Module.presses += 1
        Module.modules["broadcaster"].receive(False, None)
        while Module.process_queue:
            module, value, from_module = Module.process_queue.pop(0)
            module.receive(value, from_module)
    return reduce(lambda x, y: math.lcm(x, y), Module.important.values(), 1)


def main():
    read_in()
    # for each in Module.modules:
    #     print(each, Module.modules[each].get_output())
    # print(p1())

    Module.modules = {}
    Module.process_queue = []
    read_in()
    print(p2())


if __name__ == '__main__':
    main()
