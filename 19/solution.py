import regex


def part2():
    rules[8] = '42 +'
    rules[11] = '(?P<group> 42 (?&group)? 31 )'
    return part1()


def part1():
    def create_regex():
        def expand(r):
            return get_regex(int(r)) if r.isdigit() else r

        def get_regex(rule_id):
            return '(' + ''.join(map(expand, rules.get(rule_id).split())) + ')'

        return get_regex(0)

    valid_messages = messages.copy()
    reg = regex.compile(create_regex())
    for message in messages:
        if not reg.fullmatch(message):
            valid_messages.remove(message)
    return len(valid_messages)


def parse(data):
    rule_message_separator = data.index('')
    rules = {}
    messages = []
    for index, line in enumerate(data):
        if index < rule_message_separator:
            split_rule = line.split(': ')
            rules[int(split_rule[0])] = split_rule[1].replace('"', '')
        if index > rule_message_separator:
            messages.append(line)
    return rules, messages


if __name__ == '__main__':
    rules, messages = parse([line.strip() for line in open('data.txt')])
    print('Part 1', part1())
    print('Part 2', part2())
