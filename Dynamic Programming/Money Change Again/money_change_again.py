# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
  if money == 0:
     return 0
  best = -1
  if money == 1 or money == 3 or money == 4:
      best = 1
  elif money ==2:
      best = 2
  else:
      k = money - 4
      if k/4 > k//4:
          k = k//4 + 1
      else:
          k = k//4
      best = 1 + k
  return best


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
