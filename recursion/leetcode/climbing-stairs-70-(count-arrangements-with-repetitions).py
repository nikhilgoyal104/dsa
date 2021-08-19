# T=2ⁿ,S=n
def x(n):
    if not n:
        return 1
    if n < 0:
        return 0
    count = 0
    for val in [1, 2]:
        count += x(n - val)
    return count


for n in [
    2, 3, 6
]:
    print(x(n), end=' ')

print()


# T=n,S=n
def y(n, dp):
    if n in dp:
        return dp[n]
    if n < 0:
        return 0
    dp[n] = 0
    for val in [1, 2]:
        dp[n] += y(n - val, dp)
    return dp[n]


# T=n,S=n
def z(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for target in range(1, n + 1):
        for coin in [1, 2]:
            if target >= coin:
                dp[target] += dp[target - coin]
    return dp[-1]


for n in [
    2, 3, 6, 35, 45
]:
    print(y(n, {0: 1}), end=' ')
    print(z(n))
