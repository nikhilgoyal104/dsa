def x(m, n):
    dp = {(m - 1, n - 1): 1}

    def dfs(ri, ci):
        if ri == m or ci == n:
            return 0
        key = ri, ci
        if key in dp:
            return dp[key]
        dp[key] = 0
        for i, j in (1, 0), (0, 1):
            dp[key] += dfs(ri + i, ci + j)
        return dp[key]

    return dfs(0, 0)


def y(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


for m, n in [
    (3, 7),
    (3, 2),
    (7, 3),
    (3, 3)
]:
    print(x(m, n), end=' ')
    print(y(m, n))
