# python3

from sys import stdin


def maximum_gold(capacity, weights):
    # assert 1 <= capacity <= 10 ** 4
    # assert 1 <= len(weights) <= 10 ** 3
    # assert all(1 <= w <= 10 ** 5 for w in weights)

    if capacity == 0 or len(weights)==0:
        return 0
    array = [0]*len(weights)
    for i in range(len(weights)):
        array[i]=[]
        for j in range(capacity+1):
            if i == 0:
              if j < weights[i]:
                 array[i].append(0)
              if j >= weights[i]:
                array[i].append(weights[i])
            else:
               array[i].append(array[i-1][j])
            #   print(type(weights[i]))
            #   print(type(array[i-1][j]))
            #   print(type(j))
               if j-weights[i]>=0:
                   if weights[i] + array[i-1][j-weights[i]] <= j and weights[i] + array[i-1][j-weights[i]] > array[i][j]:
                       array[i][j] = weights[i] + array[i-1][j-weights[i]]


    #print(array)
    return array[-1][-1]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
