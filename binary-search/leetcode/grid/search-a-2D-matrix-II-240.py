# T=mn,S=1
def x(grid, target):
    for row in grid:
        if target in row:
            return True
    return False


# T=m+n,S=1
def y(grid, target):
    m, n = len(grid), len(grid[0])
    ri, ci = 0, n - 1
    while ri < m and ci > -1:
        if target == grid[ri][ci]:
            return True
        elif target > grid[ri][ci]:
            ri += 1
        else:
            ci -= 1
    return False


for grid, target in [
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5),
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20)
]:
    print(x(grid, target), end=' ')
    print(y(grid, target))
