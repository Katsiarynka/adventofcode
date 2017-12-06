import os
cur_dir = os.path.dirname(os.path.abspath(__file__))

data = open('%s/sources/day4.txt' % cur_dir).read()


def validate_passwords():
    valid_passwords = 0
    for line in data.split('\n'):
        values = sorted([v for v in line.split()])
        set_values = list(set(values))
        is_valid = len(values) == len(set_values)
        valid_passwords += int(is_valid)
    return valid_passwords

# print(validate_passwords())


def validate_words():
    valid_words = 0
    for line in data.split('\n'):
        values = sorted([v for v in line.split()])
        is_valid = True
        set_values = set()
        for value in values:
            set_value = ''.join(sorted([letter for letter in value]))
            if set_value not in set_values:
                set_values.add(set_value)
            else:
                is_valid = False
                break
        valid_words += int(is_valid)

    return valid_words


print(validate_words())