def get_destination(from_cup, selected_cups, max_cup):
    cup_number_to_check = from_cup - 1 if from_cup - 1 != 0 else max_cup
    if cup_number_to_check in selected_cups:
        return get_destination(cup_number_to_check, selected_cups, max_cup)
    else:
        return cup_number_to_check


def play(game_cups, current_cup, max_cup):
    cup1 = game_cups[current_cup]
    cup2 = game_cups[cup1]
    cup3 = game_cups[cup2]
    dest_cup = get_destination(current_cup, [cup1, cup2, cup3], max_cup)
    game_cups[current_cup], game_cups[dest_cup], game_cups[cup3] = game_cups[cup3], cup1, game_cups[dest_cup]
    return game_cups[current_cup]


def part2():
    game_cups = cups_neighbors.copy()
    game_cups[list(game_cups.keys())[-1]] = 10
    game_cups[1000000] = list(game_cups.keys())[0]
    for i in range(10, 1000000):
        game_cups[i] = i + 1

    max_cup = max(game_cups)
    current_cup = list(game_cups.keys())[0]
    for _ in range(10000000):
        current_cup = play(game_cups, current_cup, max_cup)

    first_cup = game_cups[1]
    second_cup = game_cups[first_cup]
    return first_cup * second_cup


def part1():
    game_cups = cups_neighbors.copy()

    max_cup = max(game_cups)
    current_cup = list(game_cups.keys())[0]
    for _ in range(100):
        current_cup = play(game_cups, current_cup, max_cup)

    result = ''
    c = 1
    for _ in range(len(game_cups) - 1):
        result += str(game_cups[c])
        c = game_cups[c]
    return result


def parse(cup_order):
    neighbor_mapping = {}
    for i, cup in enumerate(cup_order):
        neighbor_mapping[cup] = cup_order[(i + 1) % len(cup_order)]
    return neighbor_mapping


if __name__ == '__main__':
    cups_neighbors = parse(list(map(lambda x: int(x), ' '.join(open('data.txt').readline()).split())))
    print('Part 1', part1())
    print('Part 2', part2())
