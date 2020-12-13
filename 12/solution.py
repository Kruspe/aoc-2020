def part2():
    waypoint = [1, 10]
    manhattan_distance = [0, 0]

    def rotate_waypoint():
        if instruction[1] % 360 == 180:
            return [-waypoint[0], -waypoint[1]]
        if instruction[0] == 'L':
            if instruction[1] % 360 == 90:
                return [waypoint[1], -waypoint[0]]
            if instruction[1] % 360 == 270:
                return [-waypoint[1], waypoint[0]]
        if instruction[0] == 'R':
            if instruction[1] % 360 == 90:
                return [-waypoint[1], waypoint[0]]
            if instruction[1] % 360 == 270:
                return [waypoint[1], -waypoint[0]]

    def move():
        return [manhattan_distance[0] + instruction[1] * waypoint[0],
                manhattan_distance[1] + instruction[1] * waypoint[1]]

    def move_waypoint():
        if instruction[0] == 'N':
            return [waypoint[0] + instruction[1], waypoint[1]]
        if instruction[0] == 'E':
            return [waypoint[0], waypoint[1] + instruction[1]]
        if instruction[0] == 'S':
            return [waypoint[0] - instruction[1], waypoint[1]]
        if instruction[0] == 'W':
            return [waypoint[0], waypoint[1] - instruction[1]]

    for instruction in instructions:
        if instruction[0] == 'F':
            manhattan_distance = move()
        elif instruction[0] == 'L' or instruction[0] == 'R':
            waypoint = rotate_waypoint()
        else:
            waypoint = move_waypoint()
    return abs(manhattan_distance[0]) + abs(manhattan_distance[1])


def part1():
    degree_direction_mapping = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
    facing = 90
    manhattan_distance = [0, 0]

    def rotate():
        if instruction[0] == 'L':
            return (facing - instruction[1]) % 360
        else:
            return (facing + instruction[1]) % 360

    def move(direction):
        if direction == 'N':
            manhattan_distance[0] += instruction[1]
        if direction == 'E':
            manhattan_distance[1] += instruction[1]
        if direction == 'S':
            manhattan_distance[0] -= instruction[1]
        if direction == 'W':
            manhattan_distance[1] -= instruction[1]

    for instruction in instructions:
        if instruction[0] == 'L' or instruction[0] == 'R':
            facing = rotate()
        elif instruction[0] == 'F':
            move(degree_direction_mapping.get(facing))
        else:
            move(instruction[0])
    return abs(manhattan_distance[0]) + abs(manhattan_distance[1])


if __name__ == '__main__':
    instructions = []
    [instructions.append((instruction.strip()[0], int(instruction.strip()[1:]))) for instruction in open('data.txt')]
    print('Part 1', part1())
    print('Part 2', part2())
