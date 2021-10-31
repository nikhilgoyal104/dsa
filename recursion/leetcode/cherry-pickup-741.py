from math import inf

grids = [
    [[0, 1, -1], [1, 0, -1], [1, 1, 1]],
    [
        [1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1]
    ],
    [[1, 1, -1], [1, -1, 1], [-1, 1, 1]]
]


def invalid(grid, r1, c1, r2, c2):
    m, n = len(grid), len(grid[0])
    return r1 == n or r2 == n or c1 == m or c2 == m or grid[r1][c1] == -1 or grid[r2][c2] == -1


def main(grid):
    m, n = len(grid), len(grid[0])

    def dfs(r1, c1, r2, c2):
        if invalid(grid, r1, c1, r2, c2):
            return -inf
        if r1 == m - 1 and c1 == n - 1:
            return grid[r1][c1]
        cherries = grid[r1][c1] if (r1, c1) == (r2, c2) else grid[r1][c1] + grid[r2][c2]
        cherries += max(dfs(r1 + 1, c1, r2 + 1, c2), dfs(r1 + 1, c1, r2, c2 + 1),
                        dfs(r1, c1 + 1, r2 + 1, c2), dfs(r1, c1 + 1, r2, c2 + 1))
        return cherries

    res = dfs(0, 0, 0, 0)
    return 0 if res == -inf else res


for grid in grids:
    print(main(grid), end=' ')

print()


def main(grid):
    m, n = len(grid), len(grid[0])
    dp = {(m - 1, n - 1, m - 1, n - 1): grid[m - 1][n - 1]}

    def dfs(r1, c1, r2, c2):
        if invalid(grid, r1, c1, r2, c2):
            return -inf
        key = r1, c1, r2, c2
        if key in dp:
            return dp[key]
        dp[key] = grid[r1][c1] if (r1, c1) == (r2, c2) else grid[r1][c1] + grid[r2][c2]
        dp[key] += max(dfs(r1 + 1, c1, r2 + 1, c2), dfs(r1 + 1, c1, r2, c2 + 1),
                       dfs(r1, c1 + 1, r2 + 1, c2), dfs(r1, c1 + 1, r2, c2 + 1))
        return dp[key]

    res = dfs(0, 0, 0, 0)
    return 0 if res == -inf else res


for grid in grids:
    print(main(grid), end=' ')
