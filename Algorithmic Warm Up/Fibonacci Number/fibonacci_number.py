# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    fibArray = [0, 1]
    counter = n - 1
    while counter > 0:
        fibArray.append(fibArray[-1]+fibArray[-2])
        counter-= 1;
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibArray[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
