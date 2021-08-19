from math import inf, sqrt


# T=n√n,S=n
def x(n):
    coins = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]
    dp = [inf] * (n + 1)
    dp[0] = 0
    for target in range(1, n + 1):
        for coin in coins:
            if coin > target:
                break
            dp[target] = min(dp[target], 1 + dp[target - coin])
    return dp[-1]


# T=n√n,S=n
def y(n):
    coins = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]
    dp = [inf] * (n + 1)
    dp[0] = 0
    for coin in coins:
        for target in range(coin, n + 1):
            dp[target] = min(dp[target], 1 + dp[target - coin])
    return dp[-1]


for n in [
    12, 13, 40, 143, 6554, 7168
]:
    print(x(n), end=' ')
    print(y(n))
