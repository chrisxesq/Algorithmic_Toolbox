# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0




def majority_element(elements):
    dic = {}
    for x in range(0, len(elements)):
        if elements[x] in dic.keys():
            dic[elements[x]] += 1
        else:
            dic[elements[x]]=1
    if len(elements) % 2 == 0:
        major = len(elements) // 2
        for val in dic.values():
          if val > major:
            return 1
    else:
        major = len(elements)//2 + 1
        for val in dic.values():
          if val >= major:
            return 1
    return 0




if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
