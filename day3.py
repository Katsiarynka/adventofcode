from collections import defaultdict

number = 347991


def get_setps_to_center(number):
    steps = 0
    steps_to_center = 0
    for i in range(1, 1001, 2):
        if i * i >= number:
            line = number - (i - 2) * (i - 2)
            rest = line % (i - 1)
            steps = steps_to_center + abs((i // 2 + 1) - rest - 1)
            break
        steps_to_center += 1
    return steps


# print(get_setps_to_center(number))


def get_larger_number_in_spiral(number):
    array = defaultdict(dict)
    radius = 1
    curr_y = curr_x = result = 0
    for i in range(1000):
        if result > number:
            break
        if i == 0:
            array[curr_y][curr_x] = 1
            curr_x += 1
            continue
        result = sum([array[curr_y].get(curr_x + 1, 0), array[curr_y].get(curr_x - 1, 0),
                 array[curr_y + 1].get(curr_x + 1, 0), array[curr_y + 1].get(curr_x - 1, 0),
                 array[curr_y - 1].get(curr_x + 1, 0), array[curr_y - 1].get(curr_x - 1, 0),
                 array[curr_y + 1].get(curr_x, 0), array[curr_y - 1].get(curr_x, 0)])

        array[curr_y][curr_x] = result
        if curr_x == radius and curr_y == -radius:
            radius += 1
            curr_x = radius
        else:
            curr_y, curr_x = get_next_indexes(curr_y, curr_x, radius)
        print(curr_y, curr_x, result)
    return result


def get_next_indexes(y, x, radius):
    curr_y, curr_x = y, x
    if abs(curr_x) == radius and abs(curr_y) != radius:
        curr_y = int(curr_x / radius) + curr_y
    else:
        curr_x = int(-1 * curr_y / radius) + curr_x
    return curr_y, curr_x


print(get_larger_number_in_spiral(number))

