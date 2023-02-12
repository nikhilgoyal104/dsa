grids = [
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
    [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
    [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
]


# T=mn,S=m+n
def main(grid):
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


for grid in grids:
    print(main(grid))

print()


# T=mn,S=1
def main(grid):
    m, n = len(grid), len(grid[0])
    firstRow, firstCol = False, False
    for i in range(m):
        for j in range(n):
            if not grid[i][j]:
                if not i:
                    firstRow = True
                if not j:
                    firstCol = True
                grid[i][0] = grid[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if not grid[i][0] or not grid[0][j]:
                grid[i][j] = 0
    if firstRow:
        for j in range(n):
            grid[0][j] = 0
    if firstCol:
        for i in range(m):
            grid[i][0] = 0


for grid in grids:
    main(grid)
    print(grid)
