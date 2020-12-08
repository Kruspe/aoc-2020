def fix_instructions(instructions):
    _, executed_lines = run_program(instructions)
    for index in executed_lines:
        altered_instructions = instructions.copy()
        if instructions[index].split()[0] == 'jmp':
            altered_instructions[index] = altered_instructions[index].replace('jmp', 'nop')
            result, _ = run_program(altered_instructions)
            if result[1]:
                return result
        if instructions[index].split()[0] == 'nop':
            altered_instructions[index] = altered_instructions[index].replace('nop', 'jmp')
            result, _ = run_program(altered_instructions)
            if result[1]:
                return result



def run_program(instructions):
    executed_lines = []

    def run(line, accumulator):
        if line >= len(instructions):
            return accumulator, True
        if line in executed_lines:
            return accumulator, False

        instruction = instructions[line].split()
        executed_lines.append(line)
        if instruction[0] == 'nop':
            return run(line + 1, accumulator)
        elif instruction[0] == 'jmp':
            return run(line + int(instruction[1]), accumulator)
        else:
            return run(line + 1, accumulator + int(instruction[1]))

    return run(0, 0), executed_lines


if __name__ == '__main__':
    instructions = [rule.strip() for rule in open('data.txt')]
    print('Part 1:', run_program(instructions)[0])
    print('Part 2:', fix_instructions(instructions))
