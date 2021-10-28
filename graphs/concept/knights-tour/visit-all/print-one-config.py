def outside(n, ri, ci):
    return ri > n - 1 or ci > n - 1 or ri < 0 or ci < 0


def main(n, sri, sci):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    offsets = (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)

    def dfs(ri, ci, move):
        if outside(n, ri, ci) or grid[ri][ci]:
            return False
        grid[ri][ci] = move
        if move == n * n:
            print(grid)
            return True
        for i, j in offsets:
            if dfs(ri + i, ci + j, move + 1):
                return True
        grid[ri][ci] = 0
        return False

    dfs(sri, sci, 1)


for n, sri, sci in [(5, 2, 0), (5, 0, 0), (4, 0, 0), (4, 2, 0)]:
    main(n, sri, sci)
