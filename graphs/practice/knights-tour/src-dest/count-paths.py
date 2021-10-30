inputs = [
    (3, 3, 0, 0, 2, 2)
]


def outside(m, n, ri, ci):
    return ri > m - 1 or ci > n - 1 or ri < 0 or ci < 0


def main(m, n, sri, sci, dri, dci):
    grid = [[0 for _ in range(n)] for _ in range(m)]
    offsets = (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)

    def dfs(ri, ci, move):
        if outside(m, n, ri, ci) or grid[ri][ci]:
            return 0
        if (ri, ci) == (dri, dci):
            grid[ri][ci] = move
            print(grid)
            grid[ri][ci] = 0
            return 1
        grid[ri][ci] = move
        res = 0
        for i, j in offsets:
            res += dfs(ri + i, ci + j, move + 1)
        grid[ri][ci] = 0
        return res

    return dfs(sri, sci, 1)


for m, n, sri, sci, dri, dci in inputs:
    print(main(m, n, sri, sci, dri, dci))


def main(m, n, sri, sci, dri, dci):
    vis = set()
    offsets = (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)

    def dfs(ri, ci):
        if outside(m, n, ri, ci) or (ri, ci) in vis:
            return 0
        if (ri, ci) == (dri, dci):
            return 1
        vis.add((ri, ci))
        res = 0
        for i, j in offsets:
            res += dfs(ri + i, ci + j)
        vis.remove((ri, ci))
        return res

    return dfs(sri, sci)


for m, n, sri, sci, dri, dci in inputs:
    print(main(m, n, sri, sci, dri, dci))
