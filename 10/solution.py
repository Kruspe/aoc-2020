import functools
import operator

import math


def possibilities_for_each_step(sorted_adapters):
    possibilities = []
    for adapter in sorted_adapters[:-1]:
        options = 0
        for i in range(1, 4):
            if (adapter + i) in sorted_adapters:
                options += 1
        possibilities.append(str(options))
    return possibilities


def longest_streak_of_threes(difference_string):
    high_score = 0
    temp = 0
    for c in difference_string:
        if c == '3':
            temp += 1
        else:
            if temp > high_score:
                high_score = temp
            temp = 0
    return high_score


def count_streaks_of_threes(max_amount, difference_string):
    streaks = {}
    for i in range(1, max_amount + 1).__reversed__():
        streaks[i] = difference_string.count('3' * i)
    for key in list(streaks.keys())[1:]:
        streaks[key] = streaks[key] - (key + 1) * streaks[key + 1]
    return streaks


def calculate_number_of_combinations(sorted_adapters):
    possibilities = ''.join(possibilities_for_each_step(sorted_adapters))
    max_streak_length = longest_streak_of_threes(possibilities)
    streaks = count_streaks_of_threes(max_streak_length, possibilities)
    multiplier_list = []
    for streak in streaks.items():
        multiplier_list.append(math.pow(sum(list(range(1, streak[0]))) * 3 + 4, streak[1]))
    multiplier_list.append(math.pow(2, possibilities.count('2') - sum(streaks.values())))
    return functools.reduce(operator.mul, multiplier_list)


def count_possibilities(sorted_adapters):
    def count(n):
        if n == sorted_adapters[-1]:
            return 1
        options = 0
        for i in range(1, 4):
            if (n + i) in sorted_adapters:
                options += count(n + i)
        return options

    return count(0)


def jolt_differences(sorted_adapters):
    return [y - x for (x, y) in zip(sorted_adapters, sorted_adapters[1:])]


if __name__ == '__main__':
    adapters = [int(adapter.strip()) for adapter in open('data.txt')]
    adapters.extend([0, max(adapters) + 3])
    differences = jolt_differences(sorted(adapters))
    print('Part 1:', differences.count(1) * differences.count(3))
    print('Part 2:', calculate_number_of_combinations(sorted(adapters)))
