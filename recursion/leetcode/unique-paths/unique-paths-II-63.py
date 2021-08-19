# T=mn,S=mn
def x(grid):
    m, n = len(grid), len(grid[0])
    dp = {(m - 1, n - 1): 1}

    def dfs(ri, ci):
        if ri == m or ci == n or grid[ri][ci]:
            return 0
        key = ri, ci
        if key in dp:
            return dp[key]
        dp[key] = 0
        for i, j in (1, 0), (0, 1):
            dp[key] += dfs(ri + i, ci + j)
        return dp[key]

    return dfs(0, 0)


# T=mn,S=1
def y(grid):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        grid[i][0] = 0 if grid[i][0] else 1
    for j in range(n):
        grid[0][j] = 0 if grid[0][j] else 1
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = 0 if grid[i][j] else grid[i - 1][j] + grid[i][j - 1]
    return grid[-1][-1]


for grid in [
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ],
    [
        [0, 1],
        [0, 0]
    ]
]:
    print(x(grid), end=' ')
    print(y(grid))
