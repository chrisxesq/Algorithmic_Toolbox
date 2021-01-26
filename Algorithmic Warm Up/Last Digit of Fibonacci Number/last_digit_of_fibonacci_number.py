# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    fibarray = [0, 1]
    counter = n - 1
    while counter > 0:
        fibarray.append((fibarray[-1]+fibarray[-2]) % 10)
        counter -= 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibarray[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
