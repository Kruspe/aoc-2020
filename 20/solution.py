from collections import defaultdict
from functools import reduce
from operator import mul

import numpy as np
from math import sqrt


def flip_rotate(i):
    return [i, np.rot90(i), np.rot90(i, 2), np.rot90(i, 3), np.flipud(i), np.fliplr(i), np.flipud(np.rot90(i)),
            np.fliplr(np.rot90(i))]


def part2():
    def count_sea_monsters():
        def is_sea_monster(rows_to_check):
            for m, n in enumerate(sea_monster):
                for o in n:
                    if rows_to_check[m][o] != '#':
                        return False
            return True

        sea_monster = [[18], [0, 5, 6, 11, 12, 17, 18, 19], [1, 4, 7, 10, 13, 16]]

        for flip in flip_rotate(whole_image):
            steps = 20 * (int(len(flip) / 20) - 1) + len(flip) % 20
            sea_monster_counter = 0

            for j in range(len(flip) - 2):
                for k in range(steps):
                    rows = []
                    for row_to_check in flip[j:3 + j]:
                        rows.append(row_to_check[k:20 + k])
                    if is_sea_monster(rows):
                        sea_monster_counter += 1
            if sea_monster_counter > 0:
                return sea_monster_counter

    def get_neighbors(id, image_to_check):
        left_border = image_to_check[:, 0]
        top_border = image_to_check[0, :]
        right_border = image_to_check[:, -1]
        bottom_border = image_to_check[-1, :]
        neighbor_map = defaultdict(lambda: (None, None))
        for other_image_id, other_image in images.items():
            if not id == other_image_id:
                for flipped_other_image in flip_rotate(other_image):
                    if np.array_equal(left_border, flipped_other_image[:, -1]):
                        neighbor_map['left'] = (other_image_id, flipped_other_image)
                    if np.array_equal(top_border, flipped_other_image[-1, :]):
                        neighbor_map['top'] = (other_image_id, flipped_other_image)
                    if np.array_equal(right_border, flipped_other_image[:, 0]):
                        neighbor_map['right'] = (other_image_id, flipped_other_image)
                    if np.array_equal(bottom_border, flipped_other_image[0, :]):
                        neighbor_map['bottom'] = (other_image_id, flipped_other_image)
        return image_to_check, neighbor_map

    def put_correct_image(row, column):
        image_to_insert = resulting_image_ids[row, column]
        if row == 0:
            left_neighbor_id = resulting_image_ids[row, column - 1]
            left_neighbor_border = resulting_image[row, column - 1][:, -1]
            for flip in flip_rotate(images[image_to_insert]):
                if resulting_image[row, column] is not None:
                    break
                if np.array_equal(flip[:, 0], left_neighbor_border):
                    resulting_image[row, column] = flip
                    for possibility in possible_neighbors[image_to_insert]:
                        if possibility[1]['left'][0] == left_neighbor_id and \
                                possibility[1]['bottom'][0] is not None and possibility[1]['right'][0] is not None:
                            resulting_image_ids[row + 1, column] = possibility[1]['bottom'][0]
                            resulting_image_ids[row, column + 1] = possibility[1]['right'][0]
                            break
        if column == 0:
            top_neighbor_id = resulting_image_ids[row - 1, column]
            top_neighbor_border = resulting_image[row - 1, column][-1, :]
            for flip in flip_rotate(images[image_to_insert]):
                if resulting_image[row, column] is not None:
                    break
                if np.array_equal(flip[0, :], top_neighbor_border):
                    resulting_image[row, column] = flip
                    for possibility in possible_neighbors[image_to_insert]:
                        if possibility[1]['top'][0] == top_neighbor_id and \
                                possibility[1]['bottom'][0] is not None and possibility[1]['right'][0] is not None:
                            resulting_image_ids[row + 1, column] = possibility[1]['bottom'][0]
                            resulting_image_ids[row, column + 1] = possibility[1]['right'][0]
                            break
        if row > 0 and column > 0:
            top_neighbor_id = resulting_image_ids[row - 1, column]
            left_neighbor_id = resulting_image_ids[row, column - 1]
            top_neighbor_border = resulting_image[row - 1, column][-1, :]
            left_neighbor_border = resulting_image[row, column - 1][:, -1]
            for flip in flip_rotate(images[image_to_insert]):
                if resulting_image[row, column] is not None:
                    break
                if np.array_equal(flip[0, :], top_neighbor_border) and np.array_equal(flip[:, 0], left_neighbor_border):
                    resulting_image[row, column] = flip
                    for possibility in possible_neighbors[image_to_insert]:
                        if row != final_image_length - 1 and column != final_image_length - 1:
                            if possibility[1]['top'][0] == top_neighbor_id and \
                                    possibility[1]['left'][0] == left_neighbor_id and \
                                    possibility[1]['bottom'][0] is not None and possibility[1]['right'][0] is not None:
                                resulting_image_ids[row + 1, column] = possibility[1]['bottom'][0]
                                resulting_image_ids[row, column + 1] = possibility[1]['right'][0]
                                break
                        elif row == final_image_length - 1:
                            if possibility[1]['top'][0] == top_neighbor_id and \
                                    possibility[1]['left'][0] == left_neighbor_id and \
                                    possibility[1]['right'][0] is not None:
                                resulting_image_ids[row, column + 1] = possibility[1]['right'][0]
                                break
                        else:
                            if possibility[1]['top'][0] == top_neighbor_id and \
                                    possibility[1]['left'][0] == left_neighbor_id and \
                                    possibility[1]['bottom'][0] is not None:
                                resulting_image_ids[row + 1, column] = possibility[1]['bottom'][0]
                                break

    possible_neighbors = defaultdict(lambda: [])
    for image_id, image in images.items():
        for flipped_image in flip_rotate(image):
            possible_neighbors[image_id].append(get_neighbors(image_id, flipped_image))

    final_image_length = int(sqrt(len(images)))
    resulting_image = np.full((final_image_length, final_image_length), None)
    resulting_image_ids = np.full((final_image_length, final_image_length), None)

    for image_id, possibilities in possible_neighbors.items():
        max_neighbor_count = possibilities[0][1].keys()
        if len(max_neighbor_count) == 2:
            for possibility in possibilities:
                neighbor_positions = possibility[1].keys()
                if 'bottom' in neighbor_positions and 'right' in neighbor_positions and resulting_image[0, 0] is None:
                    resulting_image[0, 0] = possibility[0]
                    resulting_image_ids[0, 0] = image_id
                    resulting_image_ids[1, 0] = possibility[1]['bottom'][0]
                    resulting_image_ids[0, 1] = possibility[1]['right'][0]
                    break

    for y in range(final_image_length):
        for x in range(final_image_length):
            if x == 0 and y == 0:
                print('skip')
            else:
                put_correct_image(y, x)
    counted_number_symbols = 0
    for a in resulting_image:
        for b in a:
            unique, count = np.unique(b[1:-1, 1:-1], return_counts=True)
            counted_number_symbols += dict(zip(unique, count)).get('#')

    whole_image = []
    for row in resulting_image:
        for i in range(1, len(row[0]) - 1):
            new_row = ''
            for matrix in row:
                new_row = new_row + ''.join(matrix[i][1:-1])
            whole_image.append(str(' '.join(new_row)).split())

    whole_image = np.array(whole_image)
    sea_monster_count = count_sea_monsters()
    print(sea_monster_count)
    return counted_number_symbols - sea_monster_count * 15


def part1():
    def get_neighbors(id, image_to_check):
        left_border = image_to_check[:, 0]
        top_border = image_to_check[0, :]
        right_border = image_to_check[:, -1]
        bottom_border = image_to_check[-1, :]
        neighbor_map = defaultdict(lambda: [])
        for other_image_id, other_image in images.items():
            if not id == other_image_id:
                for flipped_other_image in flip_rotate(other_image):
                    if np.array_equal(left_border, flipped_other_image[:, -1]):
                        neighbor_map['left'].append(other_image_id)
                    if np.array_equal(top_border, flipped_other_image[-1, :]):
                        neighbor_map['top'].append(other_image_id)
                    if np.array_equal(right_border, flipped_other_image[:, 0]):
                        neighbor_map['right'].append(other_image_id)
                    if np.array_equal(bottom_border, flipped_other_image[0, :]):
                        neighbor_map['bottom'].append(other_image_id)
        return neighbor_map

    not_corner_pieces = set()
    for image_id, image in images.items():
        for flipped_image in flip_rotate(image):
            if len(get_neighbors(image_id, flipped_image).keys()) > 2:
                not_corner_pieces.add(image_id)
    return reduce(mul, set(images.keys()).difference(not_corner_pieces))


def parse(data):
    images_map = {}
    current_id = 0
    for line in data:
        if line.startswith('Tile'):
            current_id = int(line.replace('Tile ', '').replace(':', ''))
            images_map[current_id] = []
        elif line:
            images_map.get(current_id).append(' '.join(line).split())
    for image_id, image_data in images_map.items():
        images_map[image_id] = np.array(image_data)
    return images_map


if __name__ == '__main__':
    images = parse([line.strip() for line in open('data.txt')])
    print('Part 1', part1())
    print('Part 2', part2())
