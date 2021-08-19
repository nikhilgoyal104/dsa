from collections import deque


def main(grid):
    def dfs(ri, ci):
        if ri in [m, -1] or ci in [n, -1] or not grid[ri][ci]:
            return
        grid[ri][ci] = 0
        for i, j in (1, 0), (0, 1), (-1, 0), (0, -1):
            dfs(ri + i, ci + j)

    m, n = len(grid), len(grid[0])
    return len([dfs(ri, ci) for ci in range(n) for ri in range(m) if grid[ri][ci] == 1])


for grid in [
    [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],
    [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ],
    [
        [1, 1, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
]:
    print(main(grid))
