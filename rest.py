import time
import timeit


def find_coins_greedy(target_rest, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        count = target_rest // coin
        if count >= 1:
            target_rest = target_rest - count * coin
            result[coin] = count
    if target_rest != 0:
        raise Exception("you have no pennies to spend the rest")
    return result


def find_min_coins(target_rest, coins=[50, 25, 10, 5, 2, 1]):
    matrix = [[0 for _ in range(target_rest + 1)] for _ in range(len(coins) + 1)]
    result = {}
    for i in range(len(coins) + 1):
        for j in range(target_rest + 1):
            if i == 0 or j == 0:
                continue
            coin = coins[i - 1]
            previous_best_count = matrix[i][j - 1]
            count = target_rest // coin
            if count >= 1:
                target_rest = target_rest - count * coin
                result[coin] = count
            matrix[i][j] = previous_best_count + count
    return result


if __name__ == '__main__':
    mysetup = "from rest import find_coins_greedy"
    mycode = "find_coins_greedy(134)"

    print(timeit.timeit(setup=mysetup,
                        stmt=mycode,
                        number=10000))
    mysetup = "from rest import find_min_coins"
    mycode = "find_min_coins(134)"
    print(timeit.timeit(setup=mysetup,
                        stmt=mycode,
                        number=10000))
