def part1():
    def transform(value, subject_number):
        value *= subject_number
        return value % 20201227

    min_loop_size = 0
    card_value = 7
    door_value = 7
    while True:
        if card_value == card_pub:
            solved_for = 'card'
            break
        elif door_value == door_pub:
            solved_for = 'door'
            break

        card_value = transform(card_value, 7)
        door_value = transform(door_value, 7)
        min_loop_size += 1

    print(solved_for, min_loop_size)

    if solved_for == 'card':
        encryption_key = door_pub
        for _ in range(min_loop_size):
            encryption_key = transform(encryption_key, door_pub)
    else:
        encryption_key = card_pub
        for _ in range(min_loop_size):
            encryption_key = transform(encryption_key, card_pub)

    return encryption_key


if __name__ == '__main__':
    card_pub, door_pub = map(lambda x: int(x), [line.strip() for line in open('data.txt')])
    print('Part 1', part1())
    # print('Part 2', part2())
