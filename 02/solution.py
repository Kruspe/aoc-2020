def count_valid_passwords1(rules):
    counter = 0
    for rule in rules:
        amount, letter, password = rule.split(' ')
        min_times, max_times = map(int, amount.split('-'))
        letter = letter.replace(':', '')
        amount_letter = password.count(letter)
        if min_times <= amount_letter <= max_times:
            counter += 1
    return counter


def count_valid_passwords2(rules):
    counter = 0
    for rule in rules:
        amount, letter, password = rule.split(' ')
        index1, index2 = map(lambda x: int(x) - 1, amount.split('-'))
        letter = letter.replace(':', '')
        if sum([password[index1] == letter, password[index2] == letter]) == 1:
            counter += 1
    return counter


if __name__ == '__main__':
    rules = [rule.strip() for rule in open('data.txt')]
    correct_passwords1 = count_valid_passwords1(rules)
    correct_passwords2 = count_valid_passwords2(rules)
    print("Part 1", correct_passwords1)
    print("Part 2", correct_passwords2)
