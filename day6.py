from copy import copy
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

data = open('%s/sources/day6.txt' % cur_dir).read()


def count_of_steps():
    steps = 0
    state = []
    for line in data.split():
        state.append(int(line))
    states = list()

    len_blocks = len(state)
    while 1:
        str_state = ','.join(str(x) for x in state)
        if str_state in states:
            steps = len(states) - states.index(str_state)
            break
        states.append(str_state)

        max_value = max(state)
        index = state.index(max_value)
        state[index] = 0
        indexes = list(range(index, len_blocks)) + list(range(0, index))
        indexes = indexes[1:] + [indexes[0]]
        for i in range(max_value):
            state[indexes[i % len_blocks]] += 1

    return steps

print(count_of_steps())


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

# print(count_of_steps2())

