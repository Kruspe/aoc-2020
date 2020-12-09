import itertools


def find_sum(number, input):
    for index, _ in enumerate(input):
        for length in range(2, len(input)):
            array_sum = sum(input[index:length])
            if array_sum > number:
                break
            if array_sum == number:
                return min(input[index:length]) + max(input[index:length])


def find_first_mismatch(input, length):
    available_numbers = input[:length]
    for index in range(length, len(input)):
        if input[index] in map(lambda x: sum(x), itertools.combinations(available_numbers, 2)):
            available_numbers = input[index - length + 1:index + 1]
        else:
            return input[index]


if __name__ == '__main__':
    code = [int(rule.strip()) for rule in open('data.txt')]
    mismatch = find_first_mismatch(code, 25)
    print('Part 1:', mismatch)
    print('Part 2:', find_sum(mismatch, code))
