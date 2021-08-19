def x(n):
    grid, res = [['.'] * n for _ in range(n)], []

    def safe(grid, ri, ci):
        for i in range(ri - 1, -1, -1):
            if grid[i][ci] == 'Q':
                return False
        for i, j in zip(range(ri - 1, -1, -1), range(ci + 1, n)):
            if grid[i][j] == 'Q':
                return False
        for i, j in zip(range(ri - 1, -1, -1), range(ci - 1, -1, -1)):
            if grid[i][j] == 'Q':
                return False
        return True

    def dfs(ri):
        if ri == n:
            res.append([''.join(row) for row in grid])
            return
        for ci in range(n):
            if safe(grid, ri, ci):
                grid[ri][ci] = 'Q'
                dfs(ri + 1)
                grid[ri][ci] = '.'

    dfs(0)
    return res


# T=n!,S=n²
def y(n):
    grid = [['.'] * n for _ in range(n)]
    cols, diags, antidiags, res = set(), set(), set(), []

    def choose(ri, ci):
        cols.add(ci)
        diags.add(ri - ci)
        antidiags.add(ri + ci)
        grid[ri][ci] = 'Q'

    def discard(ri, ci):
        cols.remove(ci)
        diags.remove(ri - ci)
        antidiags.remove(ri + ci)
        grid[ri][ci] = '.'

    def dfs(ri):
        if ri == n:
            res.append([''.join(row) for row in grid])
            return
        for ci in range(n):
            if ci in cols or ri - ci in diags or ri + ci in antidiags:
                continue
            choose(ri, ci)
            dfs(ri + 1)
            discard(ri, ci)

    dfs(0)
    return res


for n in [1, 4]:
    print(x(n))
    print(y(n))
