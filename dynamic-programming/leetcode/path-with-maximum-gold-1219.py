inputs = [
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
    ],
    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
]


# T=3ᵏ,S=k
def main(grid):
    m, n = len(grid), len(grid[0])
    offsets = (0, 1), (1, 0), (-1, 0), (0, -1)

    def dfs(ri, ci, vis):
        if ri in [-1, m] or ci in [-1, n] or not grid[ri][ci] or (ri, ci) in vis:
            return 0
        vis.add((ri, ci))
        res = 0
        for i, j in offsets:
            res = max(res, grid[ri][ci] + dfs(ri + i, ci + j, vis))
        vis.remove((ri, ci))
        return res

    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                res = max(res, dfs(i, j, set()))
    return res


for grid in inputs:
    print(main(grid), end=' ')

print()


# T=3ᵏ,S=k
def main(grid):
    m, n = len(grid), len(grid[0])
    offsets = (0, 1), (1, 0), (-1, 0), (0, -1)

    def dfs(ri, ci):
        if ri in [-1, m] or ci in [-1, n] or not grid[ri][ci]:
            return 0
        gold = grid[ri][ci]
        grid[ri][ci] = 0
        res = 0
        for i, j in offsets:
            res = max(res, gold + dfs(ri + i, ci + j))
        grid[ri][ci] = gold
        return res

    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                res = max(res, dfs(i, j))
    return res


for grid in inputs:
    print(main(grid), end=' ')
