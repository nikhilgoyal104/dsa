# T=mn,S=1
def x(grid, tar):
    for row in grid:
        if tar in row:
            return True
    return False


# T=m+n,S=1
def y(grid, tar):
    m, n = len(grid), len(grid[0])
    ri, ci = 0, n - 1
    while ri < m and ci > -1:
        if tar == grid[ri][ci]:
            return True
        elif tar > grid[ri][ci]:
            ri += 1
        else:
            ci -= 1
    return False


for grid, tar in [
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5),
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20)
]:
    print(x(grid, tar), end=' ')
    print(y(grid, tar))
