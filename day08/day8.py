import math
import numpy as np


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def p1(values):
    instructions = values[0]
    repeat = len(instructions)
    map_elements = values[2:]
    m = {}
    for element in map_elements:
        m[element[0:3]] = (element[7:10], element[12:15])
    at = 'AAA'
    i = 0
    while at != 'ZZZ':
        i += 1
        move = instructions[(i - 1) % repeat]
        if move == 'L':
            at = m[at][0]
        else:
            at = m[at][1]
    return i


def all_end_z(locations):
    for l in locations:
        if l[2] != 'Z':
            return False
    return True


def p2_old(values):
    # takes too long
    instructions = values[0]
    repeat = len(instructions)
    map_elements = values[2:]
    m = {}
    at = []
    for element in map_elements:
        key = element[0:3]
        m[key] = (element[7:10], element[12:15])
        if key[2] == 'A':
            at.append(key)
    i = 0
    while not all_end_z(at):
        i += 1
        move = instructions[(i - 1) % repeat]
        if move == 'L':
            for j in range(len(at)):
                at[j] = m[at[j]][0]
        else:
            for j in range(len(at)):
                at[j] = m[at[j]][1]
    return i


def p2(values):
    instructions = values[0]
    repeat = len(instructions)
    map_elements = values[2:]
    m = {}
    starts = []
    for element in map_elements:
        key = element[0:3]
        m[key] = (element[7:10], element[12:15])
        if key[2] == 'A':
            starts.append(key)
    when = []
    for start in starts:
        at = start
        i = 0
        while at[2] != 'Z':
            i += 1
            move = instructions[(i - 1) % repeat]
            if move == 'L':
                at = m[at][0]
            else:
                at = m[at][1]
        when.append(i)
    lcm = when[0]
    for i in range(1, len(when)):
        lcm = math.lcm(lcm, when[i])
    return lcm


def main():
    values = read_in()
    print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
