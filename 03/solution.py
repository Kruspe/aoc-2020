def count_encountered_trees(all_lanes, repeat_after, right, down):
    tree_counter = 0
    current_position = 0
    for index, lane in enumerate(all_lanes):
        if down == 1 or index % down:
            current_position = (current_position + right) % repeat_after
            if lane[current_position] == '#':
                tree_counter += 1
    return tree_counter


if __name__ == '__main__':
    lanes = [lane.strip() for lane in open('data.txt')]
    trees_part1 = count_encountered_trees(lanes[1:], len(lanes[0]), 3, 1)
    trees_part2 = count_encountered_trees(lanes[1:], len(lanes[0]), 1, 1) * \
                  count_encountered_trees(lanes[1:], len(lanes[0]), 3, 1) * \
                  count_encountered_trees(lanes[1:], len(lanes[0]), 5, 1) * \
                  count_encountered_trees(lanes[1:], len(lanes[0]), 7, 1) * \
                  count_encountered_trees(lanes[1:], len(lanes[0]), 1, 2)
    print('Trees encountered:', trees_part1)
    print('Trees encountered Part 2:', trees_part2)
