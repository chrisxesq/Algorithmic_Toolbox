# python3


def money_change(money):
    change = 0
    while money >= 10:
        money -= 10
        change+= 1
    while money >= 5:
        money -= 5
        change += 1
    while money > 0:
        money -= 1
        change += 1
    return change



if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
