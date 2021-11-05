from collections import deque


def main(grid):
    m, n = len(grid), len(grid[0])
    offsets = (1, 0), (0, 1), (-1, 0), (0, -1)

    def dfs(ri, ci):
        if ri in [m, -1] or ci in [n, -1] or not grid[ri][ci]:
            return
        grid[ri][ci] = 0
        for i, j in offsets:
            dfs(ri + i, ci + j)

    res = 0
    for ri in range(m):
        for ci in range(n):
            if grid[ri][ci] == 1:
                dfs(ri, ci)
                res += 1
    return res


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
