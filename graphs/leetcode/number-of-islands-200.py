def main(grid):
    m, n = len(grid), len(grid[0])
    offsets = (1, 0), (0, 1), (-1, 0), (0, -1)
    vis = set()
    res = 0

    def dfs(ri, ci):
        if ri in [m, -1] or ci in [n, -1] or (ri, ci) in vis or not grid[ri][ci]:
            return
        vis.add((ri, ci))
        for i, j in offsets:
            dfs(ri + i, ci + j)

    for ri in range(m):
        for ci in range(n):
            if grid[ri][ci] and (ri, ci) not in vis:
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
