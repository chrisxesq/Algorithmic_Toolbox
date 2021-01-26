# python3

from random import randint


def partition3(array, left, right):
    p, x, y =  array[left], left, right
    i = x
    while i <=y :
        if array[i]<p:
            array[i], array[x] = array[x], array[i]
            i += 1
            x += 1
        elif array[i]>p:
            array[i], array[y] = array[y], array[i]
            y -= 1
        elif array[i]==p:
            i += 1

    return x,y


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1-1)
    randomized_quick_sort(array, m2+1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)

