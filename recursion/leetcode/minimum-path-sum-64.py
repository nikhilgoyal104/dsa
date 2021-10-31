from math import inf

grids = [
    [[1, 3, 1], [1, 5, 1], [4, 2, 1]],
    [[1, 2, 3], [4, 5, 6]]
]


# T=mn,S=mn
def main(grid):
    m, n, dp = len(grid), len(grid[0]), {}

    def dfs(ri, ci):
        if ri == m - 1 and ci == n - 1:
            return grid[ri][ci]
        if ri == m or ci == n:
            return inf
        key = ri, ci
        if key in dp:
            return dp[key]
        dp[key] = inf
        for i, j in (0, 1), (1, 0):
            dp[key] = min(dp[key], grid[ri][ci] + dfs(ri + i, ci + j))
        return dp[key]

    return dfs(0, 0)


for grid in grids:
    print(main(grid), end=' ')

print()


# T=mn,S=1
def main(grid):
    m, n = len(grid), len(grid[0])
    for i in range(1, m):
        grid[i][0] += grid[i - 1][0]
    for j in range(1, n):
        grid[0][j] += grid[0][j - 1]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
    return grid[-1][-1]


for grid in grids:
    print(main(grid), end=' ')
