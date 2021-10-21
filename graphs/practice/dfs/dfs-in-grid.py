from collections import deque


def outside(m, n, ri, ci):
    return ri in [-1, m] or ci in [-1, n]


def main(grid):
    vis = set()
    m, n = len(grid), len(grid[0])
    offsets = (-1, 0), (0, 1), (1, 0), (0, -1)

    def dfs(ri, ci):
        if outside(m, n, ri, ci) or (ri, ci) in vis:
            return
        vis.add((ri, ci))
        print(grid[ri][ci], end=' ')
        for i, j in offsets:
            dfs(ri + i, ci + j)

    dfs(0, 0)


for grid in [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ],
    [
        [-1, 2, 3],
        [0, 9, 8],
        [1, 0, 1]
    ]
]:
    main(grid)
    print()
