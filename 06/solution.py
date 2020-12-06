def get_answers_part2(all_answers):
    answers = []
    possible_answers = set(all_answers[0][0])
    answers_to_remove = set()
    for index, i in enumerate(all_answers):
        if i[0].isalpha():
            for possible_answer in possible_answers:
                if possible_answer not in list(i[0]):
                    answers_to_remove.add(possible_answer)
            if answers_to_remove:
                possible_answers = possible_answers.difference(answers_to_remove)
        else:
            answers.append(possible_answers) if possible_answers else None
            possible_answers = set(all_answers[index + 1][0])
            answers_to_remove = set()
    answers.append(possible_answers)
    return answers


def get_answers_part1(list):
    answers = []
    group_answers = set()
    for i in list:
        if i.isspace():
            answers.append(group_answers)
            group_answers = set()
        else:
            for answer in i.strip():
                group_answers.add(answer)
    answers.append(group_answers)
    return answers


if __name__ == '__main__':
    part1 = get_answers_part1(open('data.txt'))
    part2 = get_answers_part2([answer.strip().split('\n') for answer in open('data.txt')])
    print('Part 1:', sum(map(lambda x: len(x), part1)))
    print('Part 2:', sum(map(lambda x: len(x), part2)))
