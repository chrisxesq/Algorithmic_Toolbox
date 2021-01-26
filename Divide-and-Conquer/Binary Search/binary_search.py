# python3
import math

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    # assert 1 <= len(keys) <= 3 * 10 ** 4

    # l = 0
    # r = len(keys)-1
    #
    #
    #     if r >= l:
    #         mid = l + (r - l) // 2
    #         if arr[mid] == x:
    #             return mid
    #
    #     # If element is smaller than mid, then it
    #     # can only be present in left subarray
    #         elif arr[mid] > x:
    #             return binarySearch(arr, l, mid-1, x)
    #
    #     # Else the element can only be present
    #     # in right subarray
    #         else:
    #             return binarySearch(arr, mid + 1, r, x)
    #
    #     else:
    #     # Element is not present in the array
    #         return -1
    # return binarySearch(keys, 0, len(keys)-1, query)
    def binarySearch (arr, l, r, x):
        while r >= l:
            mid = int(l + (r - l) / 2)
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binarySearch(arr, l, mid-1, x)
            else:
                return binarySearch(arr, mid + 1, r, x)

        return -1
    return binarySearch(keys, 0, len(keys)-1, query)


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
