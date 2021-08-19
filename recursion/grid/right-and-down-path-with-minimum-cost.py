from math import inf


def x(grid):
    m, n = len(grid), len(grid[0])
    dest = grid[m - 1][n - 1]
    dp = {(m - 1, n - 1): (dest, [(m - 1, n - 1)])}

    def dfs(ri, ci):
        if ri == m or ci == n:
            return inf, []
        key = ri, ci
        if key in dp:
            return dp[key]
        mc1, mcp1 = dfs(ri + 1, ci)
        mc2, mcp2 = dfs(ri, ci + 1)
        mcost = grid[ri][ci] + min(mc1, mc2)
        mcostpath = [key] + mcp1 if mc1 < mc2 else [key] + mcp2
        dp[key] = (mcost, mcostpath)
        return dp[key]

    return dfs(0, 0)


def y(grid):
    m, n = len(grid), len(grid[0])
    dest = grid[m - 1][n - 1]
    dp = {(m - 1, n - 1): (dest, [dest])}

    def dfs(ri, ci):
        if ri == m or ci == n:
            return inf, []
        key = ri, ci
        if key in dp:
            return dp[key]
        mc1, mcp1 = dfs(ri + 1, ci)
        mc2, mcp2 = dfs(ri, ci + 1)
        val = grid[ri][ci]
        mcost = val + min(mc1, mc2)
        mcostpath = [val] + mcp1 if mc1 < mc2 else [val] + mcp2
        dp[key] = (mcost, mcostpath)
        return dp[key]

    return dfs(0, 0)


for grid in [
    [[1, 3, 1], [1, 5, 1], [4, 2, 1]],
    [[1, 2, 3], [4, 5, 6]]
]:
    print(x(grid), end=' ')
    print(y(grid))
