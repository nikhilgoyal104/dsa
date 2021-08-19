def x(n, k):
    def dfs(i):
        if i == 1:
            return k
        if i == 2:
            return k * k
        return (k - 1) * (dfs(i - 1) + dfs(i - 2))

    return dfs(n)


# T=n,S=n
def y(n, k):
    dp = {1: k, 2: k * k}

    def dfs(i):
        if i in dp:
            return dp[i]
        dp[i] = (k - 1) * (dfs(i - 1) + dfs(i - 2))
        return dp[i]

    return dfs(n)


# T=n,S=n
def z(n, k):
    if n == 1:
        return k
    dp = [0] * n
    dp[0], dp[1] = k, k * k
    for i in range(2, n):
        dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
    return dp[-1]


for n, k in [
    (4, 2),
    (3, 2),
    (1, 1),
    (7, 2),
]:
    print(x(n, k), end=' ')
    print(y(n, k), end=' ')
    print(z(n, k))
