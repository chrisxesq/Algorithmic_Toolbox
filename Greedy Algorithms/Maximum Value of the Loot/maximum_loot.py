# python3

from sys import stdin
from fractions import Fraction

def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    weight_unit = []
    for i in range(len(weights)):
        weight_unit.append([(prices[i]/weights[i]), weights[i]])
    weight_unit.sort(reverse=True)
    val = 0
    for i in range(len(weight_unit)):
        if weight_unit[i][1] <= capacity:
            capacity -= weight_unit[i][1]
            val += weight_unit[i][1] * weight_unit[i][0]

        else:
            val += capacity * weight_unit[i][0]
            capacity = 0
    return val


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
