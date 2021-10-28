from math import inf

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
            return inf
        if (ri, ci) == (dri, dci):
            grid[ri][ci] = move
            print(grid)
            grid[ri][ci] = 0
            return 0
        grid[ri][ci] = move
        res = inf
        for i, j in offsets:
            res = min(1 + dfs(ri + i, ci + j, move + 1), res)
        grid[ri][ci] = 0
        return res

    return dfs(sri, sci, 1)


for m, n, sri, sci, dri, dci in inputs:
    print(main(m, n, sri, sci, dri, dci))


def main(m, n, sri, sci, dri, dci):
    offsets = (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)
    vis = set()

    def dfs(ri, ci):
        if outside(m, n, ri, ci) or (ri, ci) in vis:
            return inf
        if (ri, ci) == (dri, dci):
            return 0
        vis.add((ri, ci))
        res = inf
        for i, j in offsets:
            res = min(1 + dfs(ri + i, ci + j), res)
        vis.remove((ri, ci))
        return res

    return dfs(sri, sci)


for m, n, sri, sci, dri, dci in inputs:
    print(main(m, n, sri, sci, dri, dci))
