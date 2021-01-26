# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d


    distance = [stops[0]]
    for i in range(len(stops)-1):
        dis = stops[i+1]-stops[i]
        distance.append(dis)
    distance.append(d-stops[-1])
    ans = 0
    cal = 0

    for j in range(len(distance)):
        cal += distance[j]
        if cal > m:
            cal = distance[j]
            ans += 1
            if cal == m:
                cal = 0
                if j < len(distance)-1:
                  ans += 1
            elif cal > m:
                return -1
        elif cal == m:
            if j < len(distance)-1:
              ans += 1
              cal = 0
        elif cal < m:
            continue
    return ans


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
