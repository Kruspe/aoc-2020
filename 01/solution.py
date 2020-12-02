import itertools

import numpy as np


def find_combination_part1(numbers):
    for index, number in enumerate(numbers):
        filtered_numbers = list(filter(lambda x: x <= 2020 - number, numbers[index + 1:]))
        for possible_number in filtered_numbers:
            if number + possible_number == 2020:
                return [number, possible_number]


def find_combination_part2(numbers):
    for i, number in enumerate(numbers):
        filtered_numbers = list(filter(lambda x: x < (2020 - number), numbers[i + 1:]))
        if len(filtered_numbers) > 1:
            for j in itertools.combinations(filtered_numbers, 2):
                if (sum(j) + number) == 2020:
                    return np.append(np.array(j), number)


if __name__ == '__main__':
    numbers = [int(number.strip()) for number in open("data.txt")]
    part1_solution = find_combination_part1(numbers)
    part2_solution = find_combination_part2(numbers)
    print("Part 1", part1_solution, "Multiply:", part1_solution[0] * part1_solution[1])
    print("Part 2", part2_solution, "Multiply:", part2_solution[0] * part2_solution[1] * part2_solution[2])
