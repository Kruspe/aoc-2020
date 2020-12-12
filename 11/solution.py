import numpy as np


def count_occupied_seats(seats):
    unique, count = np.unique(seats, return_counts=True)
    occupied_seats = dict(zip(unique, count)).get('#')
    return occupied_seats if occupied_seats else 0


def part1():
    old_seat_matrix = seat_matrix.copy()
    prev_occupied_count = count_occupied_seats(old_seat_matrix)
    new_seat_matrix = seat_matrix.copy()
    newly_occupied_count = -1
    empty_seat = 'L'
    occupied_seat = '#'

    def modify_seat():
        if old_seat_matrix[x][y] == empty_seat and adjacent_occupied_seats == 0:
            new_seat_matrix[x][y] = occupied_seat
        if old_seat_matrix[x][y] == occupied_seat and adjacent_occupied_seats - 1 >= 4:
            new_seat_matrix[x][y] = empty_seat

    while prev_occupied_count != newly_occupied_count:
        old_seat_matrix = new_seat_matrix.copy()
        prev_occupied_count = newly_occupied_count
        for x, row in enumerate(seat_matrix):
            for y, _ in enumerate(row):
                if old_seat_matrix[x][y] != '.':
                    adjacent_occupied_seats = count_occupied_seats(
                        old_seat_matrix[max(x - 1, 0):x + 2, max(y - 1, 0):y + 2])
                    modify_seat()
        newly_occupied_count = count_occupied_seats(new_seat_matrix)

    return newly_occupied_count


def part2():
    old_seat_matrix = seat_matrix.copy()
    prev_occupied_count = count_occupied_seats(old_seat_matrix)
    new_seat_matrix = seat_matrix.copy()
    newly_occupied_count = -1
    empty_seat = 'L'
    occupied_seat = '#'
    floor = '.'
    max_x, max_y = old_seat_matrix.shape

    def create_line_of_sight_matrix():

        def nw():
            for index, i in enumerate(range(0, x).__reversed__()):
                y_index = y - (index + 1)
                if y_index == -1:
                    return floor
                if old_seat_matrix[i][y_index] != floor:
                    return old_seat_matrix[i][y_index]

            return floor

        def n():
            for i in range(0, x).__reversed__():
                if old_seat_matrix[i][y] != floor:
                    return old_seat_matrix[i][y]
            return floor

        def ne():
            for index, i in enumerate(range(0, x).__reversed__()):
                y_index = y + (index + 1)
                if y_index == max_y:
                    return floor
                if old_seat_matrix[i][y_index] != floor:
                    return old_seat_matrix[i][y_index]
            return floor

        def e():
            for i in range(y + 1, max_y):
                if old_seat_matrix[x][i] != floor:
                    return old_seat_matrix[x][i]
            return floor

        def se():
            for index, i in enumerate(range(x + 1, max_x)):
                y_index = y + (index + 1)
                if i == max_x or y_index == max_y:
                    return floor
                if old_seat_matrix[i][y_index] != floor:
                    return old_seat_matrix[i][y_index]
            return floor

        def s():
            for i in range(x + 1, max_x):
                if old_seat_matrix[i][y] != floor:
                    return old_seat_matrix[i][y]
            return floor

        def sw():
            for index, i in enumerate(range(x + 1, max_x)):
                y_index = y - (index + 1)
                if i == max_x or y_index == -1:
                    return floor
                if old_seat_matrix[i][y_index] != floor:
                    return old_seat_matrix[i][y_index]
            return floor

        def w():
            for i in range(0, y).__reversed__():
                if old_seat_matrix[x][i] != floor:
                    return old_seat_matrix[x][i]
            return floor

        return np.array([[nw(), n(), ne()], [w(), floor, e()], [sw(), s(), se()]], str)

    def modify_seat():
        if old_seat_matrix[x][y] == empty_seat and adjacent_occupied_seats == 0:
            new_seat_matrix[x][y] = occupied_seat
        if old_seat_matrix[x][y] == occupied_seat and adjacent_occupied_seats >= 5:
            new_seat_matrix[x][y] = empty_seat

    while prev_occupied_count != newly_occupied_count:
        old_seat_matrix = new_seat_matrix.copy()
        prev_occupied_count = newly_occupied_count
        for x, row in enumerate(seat_matrix):
            for y, _ in enumerate(row):
                if old_seat_matrix[x][y] != '.':
                    adjacent_occupied_seats = count_occupied_seats(create_line_of_sight_matrix())
                    modify_seat()
        newly_occupied_count = count_occupied_seats(new_seat_matrix)
    return newly_occupied_count


if __name__ == '__main__':
    seat_matrix = np.genfromtxt('data.txt', dtype=str, delimiter=1, autostrip=True)
    print('Part 1', part1())
    print('Part 2', part2())
