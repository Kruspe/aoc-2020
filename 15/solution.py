def find_number(starting_numbers, number_to_find):
    spoken_numbers = {}
    prev_number = None

    def next_round(round):
        last_time = spoken_numbers.get(prev_number) if spoken_numbers.get(prev_number) else round
        new_number = round - last_time
        spoken_numbers[prev_number] = round
        return new_number

    for index, number in enumerate(starting_numbers):
        spoken_numbers[int(number)] = index + 1
        prev_number = int(number)
    for i in range(len(starting_numbers), number_to_find):
        prev_number = next_round(i)
    return prev_number


def run_example():
    for example in examples:
        print(find_number(example, 2020))
        print(find_number(example, 30000000))


if __name__ == '__main__':
    examples = [line.strip().split(',') for line in open('example.txt')]
    data = [line.strip().split(',') for line in open('data.txt')]
    # run_example()

    print('Part 1:', find_number(data[0], 2020))
    print('Part 2:', find_number(data[0], 30000000))
