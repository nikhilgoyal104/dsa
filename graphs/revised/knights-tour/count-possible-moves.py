def outside(ri, ci, m, n):
    return ri < 0 or ci < 0 or ri > m - 1 or ci > n - 1


def main(grid, sri, sci):
    m, n = len(grid), len(grid[0])
    offsets = (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)

    def dfs(ri, ci):
        res = 0
        for i, j in offsets:
            if outside(ri + i, ci + j, m, n) or grid[ri + i][ci + j]:
                continue
            res += 1
        return res

    print(dfs(sri, sci))


for grid, sri, sci in [(
        [
            [1, 0, 1, 0],
            [0, 1, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 1]
        ], 2, 2)
]:
    main(grid, sri, sri)
