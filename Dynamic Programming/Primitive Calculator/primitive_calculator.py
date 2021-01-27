# python3


def compute_operations(n):
    store = [[],[]]
    for i in range(2, n+1):
        prev = i - 1
        best = 1
        if i % 2 == 0 and len(store[prev])> len(store[i//2]):
            prev = i // 2
            best = 2
        if i % 3 == 0 and len(store[prev])> len(store[i//3]):
            prev = i // 3
            best = 3
        store.append(store[prev]+[best])
    ans = []
    ansNum=[1]
    if n > 1:
        ans = len(store[n])
        for i in range(len(store[n])):
            if store[n][i] == 1:
                ansNum.append(ansNum[i]+1)
            else:
                ansNum.append(ansNum[i]*store[n][i])

    return ansNum



if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)


