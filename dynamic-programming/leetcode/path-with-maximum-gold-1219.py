from math import inf


# T=1,S=1
def x(grid):
    m, n = len(grid), len(grid[0])

    def dfs(ri, ci, vis):
        if ri in [-1, m] or ci in [-1, n] or not grid[ri][ci] or (ri, ci) in vis:
            return 0
        vis.add((ri, ci))
        res = -inf
        for i, j in (0, 1), (1, 0), (-1, 0), (0, -1):
            res = max(res, grid[ri][ci] + dfs(ri + i, ci + j, vis))
        vis.remove((ri, ci))
        return res

    return max(dfs(i, j, set()) for i in range(m) for j in range(n) if grid[i][j])


# T=1,S=1
def y(grid):
    m, n = len(grid), len(grid[0])

    def dfs(ri, ci):
        if ri in [-1, m] or ci in [-1, n] or not grid[ri][ci]:
            return 0
        gold, grid[ri][ci], res = grid[ri][ci], 0, -inf
        for i, j in (0, 1), (1, 0), (-1, 0), (0, -1):
            res = max(res, gold + dfs(ri + i, ci + j))
        grid[ri][ci] = gold
        return res

    return max(dfs(i, j) for i in range(m) for j in range(n) if grid[i][j])


for grid in [
    [
        [0, 6, 0],
        [5, 8, 7],
        [0, 9, 0]
    ],
    [
        [1, 0, 7],
        [2, 0, 6],
        [3, 4, 5],
        [0, 3, 0],
        [9, 0, 20]
    ]
]:
    print(x(grid), end=' ')
    print(y(grid))
