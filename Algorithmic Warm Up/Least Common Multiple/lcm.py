# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    def gcd(a, b):
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
    gcd_case = gcd(a, b)
    if gcd_case == 1:
        return int(a*b)
    else:
        return int((a / gcd_case) * (b / gcd_case) * gcd_case)
if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
