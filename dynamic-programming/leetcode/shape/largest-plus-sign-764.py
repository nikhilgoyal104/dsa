# T=n³,S=len(mines)
def x(n, mines):
    banned, res = {tuple(mine) for mine in mines}, 0
    for i in range(n):
        for j in range(n):
            k = 0
            while i + k < n and j + k < n and i - k > -1 and j - k > -1 \
                    and (i + k, j) not in banned and (i - k, j) not in banned \
                    and (i, j + k) not in banned and (i, j - k) not in banned:
                k += 1
            res = max(res, k)
    return res


# T=n²,S=n²
def y(n, mines):
    banned = {tuple(mine) for mine in mines}
    res, dp = 0, [[0] * n for _ in range(n)]
    for i in range(n):
        count = 0
        for j in range(n):
            count = 0 if (i, j) in banned else count + 1
            dp[i][j] = count
        count = 0
        for j in range(n - 1, -1, -1):
            count = 0 if (i, j) in banned else count + 1
            dp[i][j] = min(dp[i][j], count)

    for j in range(n):
        count = 0
        for i in range(n):
            count = 0 if (i, j) in banned else count + 1
            dp[i][j] = min(dp[i][j], count)
        count = 0
        for i in range(n - 1, -1, -1):
            count = 0 if (i, j) in banned else count + 1
            dp[i][j] = min(dp[i][j], count)
            res = max(res, dp[i][j])
    return res


for n, mines in [
    (5, [[4, 2]]),
    (1, [[0, 0]])
]:
    print(x(n, mines), end=' ')
    print(y(n, mines))
