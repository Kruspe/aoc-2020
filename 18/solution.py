def get_inner_most_brackets(c):
    def get_max_depth():
        search_index = 0
        depth = 0
        max_depth = 0
        while search_index != len(c):
            opening = c.find('(', search_index)
            closing = c.find(')', search_index)
            if opening == -1 and closing == -1:
                break
            if opening != -1 and opening < closing:
                depth += 1
                search_index = opening + 1
            else:
                depth -= 1
                search_index = closing + 1
            if depth > max_depth:
                max_depth = depth
        return max_depth

    max_depth = get_max_depth()
    depth = 0
    search_index = 0
    inner_most_brackets = []
    while search_index != len(c):
        opening = c.find('(', search_index)
        closing = c.find(')', search_index)
        if opening == -1 and closing == -1:
            break
        if opening != -1 and opening < closing:
            depth += 1
            search_index = opening + 1
        else:
            depth -= 1
            search_index = closing + 1
        if depth == max_depth:
            inner_most_brackets.append((opening, c[opening:closing + 1]))
    return inner_most_brackets


def part2():
    def calculate(operation_without_brackets):
        done = False
        while not done:
            op_index = operation_without_brackets.split(' ').index('+') if '+' in operation_without_brackets else 1
            operation = ' '.join(operation_without_brackets.split(' ')[op_index - 1:op_index + 2])
            operation_without_brackets = operation_without_brackets.replace(operation, str(eval(operation)), 1)
            if '*' not in operation_without_brackets and '+' not in operation_without_brackets:
                done = True
        return operation_without_brackets

    result = 0
    for calculation in calculations:
        while '(' in calculation:
            brackets_to_solve = get_inner_most_brackets(calculation)
            index_offset = 0
            for start_index, bracket in brackets_to_solve:
                calculation_result = calculate(bracket[1:-1])
                replaced_value = calculation[start_index - index_offset:].replace(bracket, calculation_result, 1)
                calculation = calculation[:start_index - index_offset] + replaced_value
                index_offset += len(bracket) - len(calculation_result)
        result += int(calculate(calculation))
    return result


def part1():
    def calculate(operation_without_brackets):
        done = False
        while not done:
            operation = ' '.join(operation_without_brackets.split(' ')[:3])
            operation_without_brackets = operation_without_brackets.replace(operation, str(eval(operation)), 1)
            if '*' not in operation_without_brackets and '+' not in operation_without_brackets:
                done = True
        return operation_without_brackets

    result = 0
    for calculation in calculations:
        while '(' in calculation:
            brackets_to_solve = get_inner_most_brackets(calculation)
            index_offset = 0
            for start_index, bracket in brackets_to_solve:
                calculation_result = calculate(bracket[1:-1])
                replaced_value = calculation[start_index - index_offset:].replace(bracket, calculation_result, 1)
                calculation = calculation[:start_index - index_offset] + replaced_value
                index_offset += len(bracket) - len(calculation_result)
        result += int(calculate(calculation))
    return result


if __name__ == '__main__':
    calculations = [line.strip() for line in open('data.txt')]
    print('Part 1:', part1())
    print('Part 2:', part2())
