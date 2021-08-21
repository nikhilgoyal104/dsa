# T=mn,S=m+n
def x(grid):
    m, n = len(grid), len(grid[0])
    rows, cols = set(), set()
    for i in range(m):
        for j in range(n):
            if not grid[i][j]:
                rows.add(i)
                cols.add(j)

    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                grid[i][j] = 0
    return grid


# T=mn,S=1
def y(grid):
    m, n = len(grid), len(grid[0])
    fr, fc = False, False
    for i in range(m):
        for j in range(n):
            if not grid[i][j]:
                if not i:
                    fr = True
                if not j:
                    fc = True
                grid[i][0] = grid[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if not grid[i][0] or not grid[0][j]:
                grid[i][j] = 0

    if fr:
        for j in range(n):
            grid[0][j] = 0

    if fc:
        for i in range(m):
            grid[i][0] = 0


for grid in [
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
    [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
    [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
]:
    print(x(grid))
