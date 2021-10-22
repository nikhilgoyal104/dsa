from math import inf


def outside(m, n, ri, ci):
    return ri > m - 1 or ci > n - 1 or ri < 0 or ci < 0


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

    print(dfs(sri, sci))


for m, n, sri, sci, dri, dci in [
    (3, 3, 0, 0, 2, 2)
]:
    main(m, n, sri, sci, dri, dci)
