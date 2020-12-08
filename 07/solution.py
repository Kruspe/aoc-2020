import re
from typing import Dict


class Rule:
    amount: int
    color: str


def get_amount_contained_bags(rules, bag_color):
    amount_of_bags = []

    def get_contained_bags(color, multiplier):
        for contained_bag, amount in rules.get(color).items():
            total_amount = int(amount) * int(multiplier)
            amount_of_bags.append(total_amount)
            get_contained_bags(contained_bag, total_amount)

    get_contained_bags(bag_color, 1)
    return sum(amount_of_bags)


def get_amount_wrappers(rules, bag_color):
    possible_wrappers = set()

    def get_possible_wrappers(color):
        for rule_color, rule in rules.items():
            if color in rule:
                possible_wrappers.add(rule_color)
                get_possible_wrappers(rule_color)

    get_possible_wrappers(bag_color)
    return len(possible_wrappers)


def parse_rules(input):
    rules: Dict[str, Dict[str, int]] = {}

    for i in input:
        color, other_bags = i.split(' bags contain ')
        rules[color] = {}
        bags_inside = re.findall(r"(\d) (\w+ \w+)", other_bags)
        for number, bag_color in bags_inside:
            rules[color][bag_color] = number
    return rules


if __name__ == '__main__':
    rules = parse_rules([rule.strip() for rule in open('data.txt')])
    print('Part 1:', get_amount_wrappers(rules, 'shiny gold'))
    print('Part 2:', get_amount_contained_bags(rules, 'shiny gold'))
