# python3


def edit_distance(first_string, second_string):
    s1 = " " + first_string
    s2 = " " + second_string
    if len(s2)>len(s1):
        s1, s2 = s2, s1
    val= []
    for i in range(len(s1)):
        val.append([i])
        for j in range(1,len(s2)):
            if i == 0:
                val[i].append(j)

            else:
                best = val[i-1][j-1]
                if s1[i] == s2[j]:
                    val[i].append(best)
                else:
                    if val[i][j-1] < best:
                        best = val[i][j-1]
                    if val[i-1][j] < best:
                        best = val[i-1][j]
                    best += 1
                    val[i].append(best)
    return(val[-1][-1])



if __name__ == "__main__":
    print(edit_distance(input(), input()))


