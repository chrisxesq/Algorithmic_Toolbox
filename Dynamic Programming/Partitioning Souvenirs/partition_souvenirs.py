# python3

from itertools import product
from sys import stdin

def partition3(values):
    values = list(values)
    if sum(values) % 3 != 0:
        return 0
    target = sum(values)/3

    partition3 = [0]*3

    def search(i):
        if i == len(values):
            return 1

        for index, element in enumerate(partition3):
            if element + values[i] <= target:
                partition3[index] += values[i]
                if search(i+1) == 1:
                    return 1
                partition3[index] -= values[i]
        return 0
    return search(0)

    # other people's magic:
    # total_value = sum(items)
    # num_items = len(items)
    # each_value, mod = divmod(total_value, 3)
    #
    # if num_items < 3 or mod or max(items) > each_value:
    #     return 0
    #
    #
    # xy_length = each_value + 1
    # z_length = num_items + 1
    # T = [[([False] * z_length)[:] for _ in range(xy_length)] for _ in range(xy_length)]
    #
    #
    # T[0][0][0] = True
    #
    #
    # for z in range(1, z_length):
    #     item_value = items[z - 1]
    #
    #     for x in range(xy_length):
    #         remain1 = x - item_value
    #
    #         for y in range(xy_length):
    #             remain2 = y - item_value
    #
    #             if x == 0 and y == 0:
    #                 T[0][0][z] = True
    #
    #             elif item_value == x and True in [T[i][y][z-1] for i in range(xy_length)]:
    #                 T[x][y][z] = True
    #
    #             elif item_value == y and True in [T[x][i][z-1] for i in range(xy_length)]:
    #                 T[x][y][z] = True
    #
    #             elif T[x][y][z-1]:
    #                 T[x][y][z] = True
    #
    #             elif remain1 > 0 and T[remain1][y][z-1]:
    #                 T[x][y][z] = True
    #
    #             elif remain2 > 0 and T[x][remain2][z-1]:
    #                 T[x][y][z] = True
    # if T[each_value][each_value][num_items]==True:
    #     return 1
    # return 0




if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))

