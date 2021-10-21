def outside(m, n, ri, ci):
    return ri > m - 1 or ci > n - 1 or ri < 0 or ci < 0


def main(m, n, sri, sci, dri, dci):
    vis = set()
    offsets = (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)

    def dfs(ri, ci):
        if outside(m, n, ri, ci) or (ri, ci) in vis:
            return 0
        if (ri, ci) == (dri, dci):
            return 1
        vis.add((ri, ci))
        count = 0
        for i, j in offsets:
            count += dfs(ri + i, ci + j)
        vis.remove((ri, ci))
        return count

    print(dfs(sri, sci))


for m, n, sri, sci, dri, dci in [
    (3, 3, 0, 0, 2, 2)
]:
    main(m, n, sri, sci, dri, dci)
