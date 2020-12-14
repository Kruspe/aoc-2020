from itertools import count


def find_first_matching_schedule(requirement, start):
    def get_next_possible_time(last_time):
        time = last_time + time_to_add
        next_bus_time = time + bus_to_check[1]
        if next_bus_time % bus_to_check[0] == 0:
            return time
        else:
            return get_next_possible_time(time)

    time_to_add = requirement[0][0]
    min_time = start - (start % time_to_add)
    for i in range(1, len(requirement)):
        bus_to_check = requirement[i]

        min_time = get_next_possible_time(min_time)
        time_to_add *= bus_to_check[0]
    return min_time


def map_requirements_and_minutes(requirement_to_map):
    return list(map(lambda indexed_requirement: (int(indexed_requirement[1]), indexed_requirement[0]),
                    filter(lambda indexed_requirement: indexed_requirement[1] != 'x', enumerate(requirement_to_map))))


def find_earliest_available_bus():
    for time in count(arrival_time):
        for bus in available_buses:
            if time % bus == 0:
                return time, bus


def part2_examples():
    for requirement in enumerate([requirement.strip().split(',') for requirement in open('example2.txt')]):
        print(find_first_matching_schedule(map_requirements_and_minutes(requirement[1]), 3000))


if __name__ == '__main__':
    arrival_time = int(open('data.txt').readlines()[0].strip())
    available_buses = list(map(lambda bus: int(bus),
                               filter(lambda bus: bus != 'x', open('data.txt').readlines()[1].strip().split(','))))
    part2_requirement = open('data.txt').readlines()[1].strip().split(',')
    # part2_examples()

    earliest_bus = find_earliest_available_bus()
    print('Part 1', (earliest_bus[0] - arrival_time) * earliest_bus[1])
    print('Part 2', find_first_matching_schedule(map_requirements_and_minutes(part2_requirement), 100000000000000))
