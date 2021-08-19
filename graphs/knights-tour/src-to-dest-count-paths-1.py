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
        count = 0
        for i, j in offsets:
            count += dfs(ri + i, ci + j, move + 1)
        grid[ri][ci] = 0
        return count

    print(dfs(sri, sci, 1))


for m, n, sri, sci, dri, dci in [
    (3, 3, 0, 0, 2, 2)
]:
    main(m, n, sri, sci, dri, dci)
