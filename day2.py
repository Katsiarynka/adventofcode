import os
cur_dir = os.path.dirname(os.path.abspath(__file__))

data = open('%s/sources/day2.txt' % cur_dir).read()


check_sum = 0
for line in data.split('\n'):
    values = sorted([int(v) for v in line.split()])
    check_sum += values[-1] - values[0]

print(check_sum)


check_sum = 0
for line in data.split('\n'):
    values = sorted([int(v) for v in line.split()])
    # check_sum += sum([x // i if not x % i else 0 for x in values[index:] for index, i in enumerate(values)])
    sums = 0
    for index, i in enumerate(values[:-1]):
        sums += sum([x // i if not x % i else 0 for x in values[index+1:]])
    check_sum += sums

print(check_sum)
