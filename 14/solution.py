from itertools import product


def evaluate_program_part2():
    mask = ''
    mem = {}

    for line in lines:
        if line[0] == 'mask':
            mask = line[1]
        else:
            mem_index_bytes = f"{int(line[0].replace('mem[', '').replace(']', '')):036b}"
            bit_number = int(line[1])
            new_index = ''
            for index, bit in enumerate(mask):
                if bit == 'X':
                    new_index += 'X'
                elif bit == '1':
                    new_index += '1'
                else:
                    new_index += mem_index_bytes[index]
            for i in product(range(2), repeat=new_index.count('X')):
                replaced_index = ''
                split_index = new_index.split('X')
                print(len(i), split_index)
                for index, j in enumerate(i):
                    replaced_index += (split_index[index] + str(j))
                replaced_index += new_index[len(replaced_index):]
                mem[int(replaced_index, 2)] = bit_number
    return sum(mem.values())


def evaluate_program_part1():
    mask = ''
    mem = {}

    for line in lines:
        if line[0] == 'mask':
            mask = line[1]
        else:
            mem_index = line[0].replace('mem[', '').replace(']', '')
            bit_number = f'{int(line[1]):036b}'
            new_number = ''
            for index, bit in enumerate(mask):
                if bit == 'X':
                    new_number += bit_number[index]
                else:
                    new_number += mask[index]
            mem[mem_index] = int(new_number, 2)
    return sum(mem.values())


if __name__ == '__main__':
    lines = [line.strip().split(' = ') for line in open('data.txt')]
    print('Part 1:', evaluate_program_part1())
    print('Part 2:', evaluate_program_part2())
