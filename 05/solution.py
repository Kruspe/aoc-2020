def get_row(row_id):
    upper_bound = 127
    lower_bound = 0
    for i in row_id:
        if i == 'F':
            upper_bound = upper_bound - (upper_bound - lower_bound >> 1) - 1
        else:
            lower_bound = lower_bound + (upper_bound - lower_bound >> 1) + 1
    return lower_bound


def get_column(column_id):
    upper_bound = 7
    lower_bound = 0
    for i in column_id:
        if i == 'L':
            upper_bound = upper_bound - (upper_bound - lower_bound >> 1) - 1
        else:
            lower_bound = lower_bound + (upper_bound - lower_bound >> 1) + 1
    return lower_bound


def get_boarding_passes(input):
    passes = []
    for i in input:
        row = get_row(i[:7])
        column = get_column(i[7:])
        passes.append({'row': row, 'column': column, 'seatID': row * 8 + column})
    return passes


if __name__ == '__main__':
    passes = get_boarding_passes([i.strip() for i in open('data.txt')])
    highest_seat_id = max(map(lambda x: x['seatID'], passes))
    print('Part 1', highest_seat_id)
    sorted_seat_ids = sorted(map(lambda x: x['seatID'], passes))
    my_seat_id = sorted_seat_ids[[x - y for x, y in zip(sorted_seat_ids, sorted_seat_ids[1:])].index(-2)] + 1
    print('Part 2', my_seat_id)
