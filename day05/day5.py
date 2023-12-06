def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def add_ranges_for_section(section, ranges, almanac: list):
    start = almanac.index(section)
    try:
        end = almanac[start:].index('') + start
    except ValueError:
        end = len(almanac)
    ranges[section[0:-1]] = {}
    for r in almanac[start + 1:end]:
        (destination, source, length) = [int(v) for v in r.split()]
        ranges[section[0:-1]][source] = (destination, length)


def p1(values):
    destinations = []
    sections = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:',
                'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']
    seeds = [int(v) for v in values[0].split()[1:]]
    ranges = {}
    for section in sections:
        add_ranges_for_section(section, ranges, values)
    for seed in seeds:
        mapped_to = seed
        for section in sections:
            section_map = ranges[section[0:-1]]
            # print(section_map)
            for k, v in section_map.items():
                if mapped_to in range(k, k + v[1]):
                    mapped_to = (mapped_to - k) + v[0]
                    break
        destinations.append(mapped_to)
    return min(destinations)


def old_p2(values):
    sections = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:',
                'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']
    seed_ranges = [int(v) for v in values[0].split()[1:]]
    ranges = {}
    for section in sections:
        add_ranges_for_section(section, ranges, values)
    min_location = 9999999999999999999999
    for i in range(0, len(seed_ranges), 2):
        for seed in range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]):
            mapped_to = seed
            for section in sections:
                section_map = ranges[section[0:-1]]
                # print(section_map)
                for k, v in section_map.items():
                    if mapped_to in range(k, k + v[1]):
                        mapped_to = (mapped_to - k) + v[0]
                        break

            min_location = min(min_location, mapped_to)
    return min_location


def add_ranges_for_section_p2(section, almanac):
    start = almanac.index(section)
    try:
        end = almanac[start:].index('') + start
    except ValueError:
        end = len(almanac)
    ranges = []
    for r in almanac[start + 1:end]:
        (destination, source, length) = [int(v) for v in r.split()]
        ranges.append((source, source + length, destination))
    return ranges


def p2(almanac):
    # extract all seed ranges
    seed_input = [int(v) for v in almanac[0].split()[1:]]
    seed_ranges = []
    for i in range(0, len(seed_input), 2):
        seed_ranges.append((seed_input[i], seed_input[i] + seed_input[i + 1]))

    # seed_ranges [(start, end), (start, end)]
    sections = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:',
                'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']

    last_ranges = seed_ranges
    for section in sections:
        almanac_ranges = add_ranges_for_section_p2(section, almanac)
        next_ranges = []
        # iterate over each seed_range
        while last_ranges:
            lr = last_ranges.pop()
            matched = False
            for ar in almanac_ranges:
                # do they overlap?
                if not (lr[0] <= ar[1] and ar[0] <= lr[1]):
                    continue
                matched = True
                # they are overlapping
                lr_overlap = (max(lr[0], ar[0]), min(lr[1], ar[1]))
                shift = 0 - ar[0] + ar[2]
                nr_overlap = (lr_overlap[0] + shift, lr_overlap[1] + shift)
                next_ranges.append(nr_overlap)

                if lr[0] < ar[0]:
                    last_ranges.append((lr[0], ar[0] - 1))
                if lr[1] > ar[1]:
                    last_ranges.append((ar[1] + 1, lr[1]))
            if not matched:
                next_ranges.append(lr)

        last_ranges = next_ranges
    return min(x[0] for x in last_ranges)


def main():
    values = read_in()
    # print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
