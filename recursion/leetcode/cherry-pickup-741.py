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
    return n in [r1, r2] or m in [c1, c2] or -1 in [grid[r1][c1], grid[r2][c2]]


def main(grid):
    m, n = len(grid), len(grid[0])

    def dfs(r1, c1, r2, c2):
        if invalid(grid, r1, c1, r2, c2):
            return float('-inf')
        if r1 == m - 1 and c1 == n - 1:
            return grid[r1][c1]
        cherries = grid[r1][c1] + grid[r2][c2]
        if (r1, c1) == (r2, c2):
            cherries = grid[r1][c1]
        cherries += max(dfs(r1 + 1, c1, r2 + 1, c2), dfs(r1 + 1, c1, r2, c2 + 1),
                        dfs(r1, c1 + 1, r2 + 1, c2), dfs(r1, c1 + 1, r2, c2 + 1))
        return cherries

    res = dfs(0, 0, 0, 0)
    return 0 if res == float('-inf') else res


for grid in grids:
    print(main(grid), end=' ')

print()


def main(grid):
    m, n = len(grid), len(grid[0])
    cache = {(m - 1, n - 1, m - 1, n - 1): grid[m - 1][n - 1]}

    def dfs(r1, c1, r2, c2):
        if invalid(grid, r1, c1, r2, c2):
            return float('-inf')
        key = r1, c1, r2, c2
        if key in cache:
            return cache[key]
        cache[key] = grid[r1][c1] + grid[r2][c2]
        if (r1, c1) == (r2, c2):
            cache[key] = grid[r1][c1]
        cache[key] += max(dfs(r1 + 1, c1, r2 + 1, c2), dfs(r1 + 1, c1, r2, c2 + 1),
                          dfs(r1, c1 + 1, r2 + 1, c2), dfs(r1, c1 + 1, r2, c2 + 1))
        return cache[key]

    res = dfs(0, 0, 0, 0)
    return 0 if res == float('-inf') else res


for grid in grids:
    print(main(grid), end=' ')
