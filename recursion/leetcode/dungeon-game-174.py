from math import inf


def main(grid):
    m, n, dp = len(grid), len(grid[0]), {}

    def dfs(ri, ci):
        if ri == m - 1 and ci == n - 1:
            return 1 + (-grid[ri][ci]) if grid[ri][ci] <= 0 else 1
        if ri == m or ci == n:
            return inf
        key = ri, ci
        if key in dp:
            return dp[key]
        dp[key] = max(min(dfs(ri + 1, ci), dfs(ri, ci + 1)) - grid[ri][ci], 1)
        return dp[key]

    return dfs(0, 0)


for grid in [
    [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]],
    [[0]]
]:
    print(main(grid))
