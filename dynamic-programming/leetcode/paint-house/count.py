from math import inf


def x(n, k):
    def dfs(i):
        if i == 1:
            return k
        return (k - 1) * dfs(i - 1)

    return dfs(n)


def y(n, k):
    dp = [0] * n
    dp[0] = k
    for i in range(1, n):
        dp[i] = (k - 1) * dp[i - 1]
    return dp[-1]


for n, k in [
    (4, 3),
    (3, 3),
    (1, 3)
]:
    print(x(n, k), end=' ')
    print(y(n, k))
