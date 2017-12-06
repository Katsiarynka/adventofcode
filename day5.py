import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

data = open('%s/sources/day5.txt' % cur_dir).read()


def count_of_steps():
    steps = 0
    sources = []
    for line in data.split('\n'):
        sources.append(int(line))

    index = 0
    while 1:
        if len(sources) <= index:
            break
        sources[index] += 1
        index += sources[index] - 1
        steps += 1
    return steps

# print(count_of_steps())


def count_of_steps2():
    steps = 0
    sources = []
    for line in data.split('\n'):
        sources.append(int(line))

    index = 0
    while 1:
        if len(sources) <= index:
            break
        value = sources[index]
        term = value < 3 and 1 or -1
        sources[index] += term
        index += value
        steps += 1
    return steps

print(count_of_steps2())

