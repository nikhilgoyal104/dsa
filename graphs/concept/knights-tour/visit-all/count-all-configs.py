def outside(n, ri, ci):
    return ri > n - 1 or ci > n - 1 or ri < 0 or ci < 0


# T=8ⁿ²,S=n²
def main(n, sri, sci):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    offsets = (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)

    def dfs(ri, ci, move):
        if outside(n, ri, ci) or grid[ri][ci]:
            return 0
        grid[ri][ci] = move
        if move == n * n:
            grid[ri][ci] = 0
            return 1
        res = 0
        for i, j in offsets:
            res += dfs(ri + i, ci + j, move + 1)
        grid[ri][ci] = 0
        return res

    return dfs(sri, sci, 1)


for n, sri, sci in [
    (5, 2, 0),
    (5, 0, 0),
    (4, 0, 0),
    (4, 2, 0)
]:
    print(main(n, sri, sci))
