def part2():
    def check_tile():
        adjacent_black_tiles = 0
        if (x + 2, row) in flipped_tiles:
            adjacent_black_tiles += 1
        if (x + 1, row - 1) in flipped_tiles:
            adjacent_black_tiles += 1
        if (x - 1, row - 1) in flipped_tiles:
            adjacent_black_tiles += 1
        if (x - 2, row) in flipped_tiles:
            adjacent_black_tiles += 1
        if (x - 1, row + 1) in flipped_tiles:
            adjacent_black_tiles += 1
        if (x + 1, row + 1) in flipped_tiles:
            adjacent_black_tiles += 1

        if (x, row) in flipped_tiles:
            if adjacent_black_tiles != 1 and adjacent_black_tiles != 2:
                turn_copy.remove((x, row))
        else:
            if adjacent_black_tiles == 2:
                turn_copy.append((x, row))

    flipped_tiles = part1()

    turn_copy = flipped_tiles.copy()
    for _ in range(100):
        for row in range(min(flipped_tiles, key=lambda a: a[1])[1] - 1, max(flipped_tiles, key=lambda a: a[1])[1] + 2):
            for x in range(min(flipped_tiles)[0] - 1, max(flipped_tiles)[0] + 2):
                if x % 2 == 0 and row % 2 == 0:
                    check_tile()
                elif x % 2 == 1 and row % 2 == 1:
                    check_tile()
        flipped_tiles = turn_copy.copy()

    return len(turn_copy)


def part1():
    flipped_tiles = []
    for tile in tiles:
        x, y = 0, 0
        for direction in tile:
            if direction == 'e':
                x += 2
            elif direction == 'se':
                x += 1
                y -= 1
            elif direction == 'sw':
                x -= 1
                y -= 1
            elif direction == 'w':
                x -= 2
            elif direction == 'nw':
                x -= 1
                y += 1
            else:
                x += 1
                y += 1
        tile_to_flip = (x, y)
        flipped_tiles.remove(tile_to_flip) if tile_to_flip in flipped_tiles else flipped_tiles.append(tile_to_flip)
    return flipped_tiles


def parse(d):
    tiles_to_flip = []
    for line in d:
        current_index = 0
        tile_identifier = []
        while True:
            if current_index == len(line):
                break
            if line[current_index] == 'e' or line[current_index] == 'w':
                tile_identifier.append(line[current_index])
                current_index += 1
            else:
                tile_identifier.append(line[current_index] + line[current_index + 1])
                current_index += 2
        tiles_to_flip.append(tile_identifier)
    return tiles_to_flip


if __name__ == '__main__':
    tiles = parse([line.strip() for line in open('data.txt')])
    print('Part 1', len(part1()))
    print('Part 2', part2())
