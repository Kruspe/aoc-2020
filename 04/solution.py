import re


def validate_hgt(height):
    if height[-2:] == 'cm':
        return len(height) == 5 and 150 <= int(height[:3]) <= 193
    elif height[-2:] == 'in':
        return len(height) == 4 and 59 <= int(height[:2]) <= 76
    else:
        return False


def validate_fields(key, value):
    validations = {'byr': (lambda x: 1920 <= int(x) <= 2002),
                   'iyr': (lambda x: 2010 <= int(x) <= 2020),
                   'eyr': (lambda x: 2020 <= int(x) <= 2030),
                   'hgt': (lambda x: validate_hgt(x)),
                   'hcl': (lambda x: bool(re.search('^#[0-9a-f]{6}', x))),
                   'ecl': (lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
                   'pid': (lambda x: len(x) == 9)}
    return validations.get(key)(value)


def count_and_validate(passports):
    counter = 0
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        copy = required_fields.copy()
        for key in passport.keys():
            if key != 'cid':
                if validate_fields(key, passport.get(key)):
                    copy.remove(key)
        if not copy:
            counter += 1

    return counter


def count_valid(passports):
    counter = 0
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        copy = required_fields.copy()
        for key in passport.keys():
            if key != 'cid':
                copy.remove(key)
        if not copy:
            counter += 1

    return counter


def get_passports(list):
    all_passports = []
    passport = {}
    for i in list:
        if i.isspace():
            all_passports.append(passport)
            passport = {}
        else:
            for k in [j.split(':') for j in i.split(' ')]:
                passport[k[0].strip()] = k[1].strip()
    all_passports.append(passport)
    return all_passports


if __name__ == '__main__':
    passports = get_passports(open('data.txt'))
    valid_passports1 = count_valid(passports)
    valid_passports2 = count_and_validate(passports)
    print('Part 1:', valid_passports1)
    print('Part 2:', valid_passports2)
