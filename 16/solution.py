from typing import List, NamedTuple


class Rule(NamedTuple):
    name: str
    limitation: List[range]


def part2():
    def get_valid_tickets():
        def is_number_valid(n):
            for rule in rules:
                for r in rule.limitation:
                    if n in r:
                        return True
            return False

        def is_ticket_valid():
            all_numbers = ticket.split(',')
            for number in all_numbers:
                if not is_number_valid(int(number)):
                    return False
            return True

        valid_tickets = []
        for ticket in nearby_tickets:
            if is_ticket_valid():
                valid_tickets.append(ticket)
        return valid_tickets

    def find_matching_rule():
        def get_possible_rules():
            possible_rules = set()
            for rule in rules:
                for r in rule.limitation:
                    if int(number) in r:
                        possible_rules.add(rule.name)
            return possible_rules

        def sanitize_map(map_to_sanitize):
            def sanitize(rule_name, index_to_skip):
                for data in map_to_sanitize.items():
                    if data[0] != index_to_skip:
                        copied_rules = data[1].copy()
                        copied_rules.discard(rule_name)
                        map_to_sanitize[data[0]] = copied_rules

            for item_index, i in map_to_sanitize.items():
                if len(i) == 1:
                    sanitize(list(i)[0], item_index)

        def all_values_len_one(map_to_check):
            for i in map_to_check.values():
                if len(i) != 1:
                    return False
            return True

        rule_name_set = set([rule.name for rule in rules])
        index_rule_map = {}
        for valid_ticket in valid_tickets:
            for index, number in enumerate(valid_ticket.split(',')):
                current_possible_rules = index_rule_map.get(index) if index_rule_map.get(index) else rule_name_set
                new_possible_rules = current_possible_rules.intersection(get_possible_rules())
                index_rule_map[index] = new_possible_rules

        while not all_values_len_one(index_rule_map):
            sanitize_map(index_rule_map)
        return index_rule_map

    value = 1
    valid_tickets = get_valid_tickets()
    for entry in find_matching_rule().items():
        if 'departure' in str(entry[1]):
            value *= int(my_ticket.split(',')[int(entry[0])])
    return value


def get_sum_of_invalid_numbers():
    def is_number_valid(n):
        for rule in rules:
            for r in rule.limitation:
                if int(n) in r:
                    return True
        return False

    def get_invalid_number():
        for number in ticket.split(','):
            if not is_number_valid(number):
                return int(number)
        return 0

    sum_of_invalid_numbers = 0
    for ticket in nearby_tickets:
        sum_of_invalid_numbers += get_invalid_number()

    return sum_of_invalid_numbers


def parse(lines):
    my_ticket_separator = lines.index('your ticket:')
    nearby_ticket_separator = lines.index('nearby tickets:')

    all_rules: List[Rule] = list()
    for rule in lines[:my_ticket_separator - 1]:
        ranges: List[range] = []
        split_rule = rule.split(': ')
        for r in (i.split('-') for i in split_rule[1].split(' or ')):
            ranges.append(range(int(r[0]), int(r[1]) + 1))
        all_rules.append(Rule(split_rule[0], ranges))

    tickets = [ticket.strip() for ticket in lines[nearby_ticket_separator + 1:len(lines)]]

    return all_rules, lines[my_ticket_separator + 1], tickets


if __name__ == '__main__':
    rules, my_ticket, nearby_tickets = parse([line.strip() for line in open('data.txt')])

    print('Part 1:', get_sum_of_invalid_numbers())
    print('Part 2:', part2())
