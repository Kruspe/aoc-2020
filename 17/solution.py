from copy import deepcopy

import numpy as np


def part2():
    def count_active_cubes(x_index, y_index, z_index, w_index):
        active_state_counter = 0
        for j in range(max(w_index - 1, 0), min(cycle * 2, w_index + 2)):
            for i in range(max(z_index - 1, 0), min(cycle * 2, z_index + 2)):
                unique, count = np.unique(
                    states_before_mutation[j][i][max(y_index - 1, 0):y_index + 2, max(x_index - 1, 0): x_index + 2],
                    return_counts=True)
                active_cubes = dict(zip(unique, count)).get('#') if dict(zip(unique, count)).get('#') else 0
                active_state_counter += active_cubes
        return active_state_counter

    active_state = '#'
    inactive_state = '.'
    last_cycle_results = [[start_configuration.copy()]]
    for cycle in range(1, 7):
        states_before_mutation = []
        for w in range(cycle * 2 + 1):
            w_dimension = []
            for z in range(cycle * 2 + 1):
                new_state = np.full(
                    (start_configuration.shape[0] + 2 * cycle, start_configuration.shape[1] + 2 * cycle),
                    inactive_state, dtype=str)
                if w != 0 and w != cycle * 2:
                    if z != 0 and z != cycle * 2:
                        new_state[1:-1, 1:-1] = last_cycle_results[w - 1][z - 1]
                w_dimension.append(new_state)
            states_before_mutation.append(w_dimension)
        working_copy = deepcopy(states_before_mutation)
        for w in range(cycle * 2 + 1):
            for z, w_dimension in enumerate(states_before_mutation):
                for y, line in enumerate(w_dimension[z]):
                    for x, _ in enumerate(line):
                        active_neighbors = count_active_cubes(x, y, z, w)
                        if states_before_mutation[w][z][y, x] == active_state:
                            if active_neighbors - 1 != 2 and active_neighbors - 1 != 3:
                                working_copy[w][z][y, x] = inactive_state
                        else:
                            if active_neighbors == 3:
                                working_copy[w][z][y, x] = active_state
        last_cycle_results = deepcopy(working_copy)

    counter = 0
    for matrix in last_cycle_results:
        unique, count = np.unique(matrix, return_counts=True)
        active_cubes = dict(zip(unique, count)).get('#') if dict(zip(unique, count)).get('#') else 0
        counter += active_cubes
    return counter


def count_active_states_after_start_up():
    def count_active_cubes(x_index, y_index, z_index):
        active_state_counter = 0
        for i in range(max(z_index - 1, 0), min(cycle * 2, z_index + 2)):
            unique, count = np.unique(
                states_before_mutation[i][max(y_index - 1, 0):y_index + 2, max(x_index - 1, 0): x_index + 2],
                return_counts=True)
            active_cubes = dict(zip(unique, count)).get('#') if dict(zip(unique, count)).get('#') else 0
            active_state_counter += active_cubes
        return active_state_counter

    active_state = '#'
    inactive_state = '.'
    last_cycle_results = [start_configuration.copy()]
    for cycle in range(1, 7):
        states_before_mutation = []
        for z in range(cycle * 2 + 1):
            new_state = np.full((start_configuration.shape[0] + 2 * cycle, start_configuration.shape[1] + 2 * cycle),
                                inactive_state, dtype=str)
            if z != 0 and z != cycle * 2:
                new_state[1:-1, 1:-1] = last_cycle_results[z - 1]
            states_before_mutation.append(new_state)
        working_copy = deepcopy(states_before_mutation)
        for z in range(cycle * 2 + 1):
            for y, line in enumerate(states_before_mutation[z]):
                for x, entry in enumerate(line):
                    active_neighbors = count_active_cubes(x, y, z)
                    if states_before_mutation[z][y, x] == active_state:
                        if active_neighbors - 1 != 2 and active_neighbors - 1 != 3:
                            working_copy[z][y, x] = inactive_state
                    else:
                        if active_neighbors == 3:
                            working_copy[z][y, x] = active_state
        last_cycle_results = deepcopy(working_copy)

    counter = 0
    for matrix in last_cycle_results:
        unique, count = np.unique(matrix, return_counts=True)
        active_cubes = dict(zip(unique, count)).get('#') if dict(zip(unique, count)).get('#') else 0
        counter += active_cubes
    return counter


def parse(file):
    raw = []
    for line in file:
        raw_line = []
        for entry in line:
            raw_line.append(entry.strip())
        raw.append(raw_line)
    return np.array(raw)


if __name__ == '__main__':
    start_configuration = parse(line.strip() for line in open('data.txt'))
    print('Part 1:', count_active_states_after_start_up())
    print('Part 2:', part2())
