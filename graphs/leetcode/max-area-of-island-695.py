def outside(m, n, ri, ci):
    return ri in [-1, m] or ci in [-1, n]


def main(grid):
    m, n = len(grid), len(grid[0])
    offsets = (-1, 0), (0, 1), (1, 0), (0, -1)
    res = 0
    vis = set()

    def dfs(ri, ci):
        if outside(m, n, ri, ci) or (ri, ci) in vis or not grid[ri][ci]:
            return 0
        vis.add((ri, ci))
        count = 1
        for i, j in offsets:
            count += dfs(ri + i, ci + j)
        return count

    for ri in range(m):
        for ci in range(n):
            if grid[ri][ci] and (ri, ci) not in vis:
                res = max(res, dfs(ri, ci))
    return res


for grid in [
    [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
]:
    print(main(grid))
