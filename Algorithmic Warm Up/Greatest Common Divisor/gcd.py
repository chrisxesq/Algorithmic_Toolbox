# python3


def gcd_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

    assert False

def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9
    def gcd_inner(a,b):
        if a < b and b % a == 0:
            return a
        elif a > b and a % b == 0:
            return b
        return gcd_inner(b, a%b)
    if a == 0 or b == 0:
        return 0
    if a == b:
        return a
    else:
        return gcd_inner(a,b)

if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))
