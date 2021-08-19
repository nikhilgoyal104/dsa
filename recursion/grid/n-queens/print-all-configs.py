def x(n):
    grid = [[0] * n for _ in range(n)]
    cols, diags, antidiags = set(), set(), set()

    def dfs(ri):
        if ri == n:
            print(grid)
            return
        for ci in range(n):
            if ci in cols or ri - ci in diags or ri + ci in antidiags:
                continue
            cols.add(ci)
            diags.add(ri - ci)
            antidiags.add(ri + ci)
            grid[ri][ci] = 1
            dfs(ri + 1)
            cols.remove(ci)
            diags.remove(ri - ci)
            antidiags.remove(ri + ci)
            grid[ri][ci] = 0

    dfs(0)


for n in [1, 2, 3, 4]:
    x(n)
