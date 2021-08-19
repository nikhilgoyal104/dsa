def transpose(grid):
    n = len(grid)
    for i in range(n):
        for j in range(i + 1, n):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]


def reverse(grid):
    n = len(grid)
    for i in range(n):
        low, high = 0, n - 1
        while low < high:
            grid[i][low], grid[i][high] = grid[i][high], grid[i][low]
            low, high = low + 1, high - 1


def rotate(grid):
    transpose(grid)
    reverse(grid)


# T=n²,S=1
def x(grid, tar):
    for _ in range(4):
        rotate(grid)
        if grid == tar:
            return True
    return False


for grid, tar in [
    ([[0, 1], [1, 0]], [[1, 0], [0, 1]]),
    ([[0, 1], [1, 1]], [[1, 0], [0, 1]]),
    ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]])
]:
    print(x(grid, tar))

print()


# T=n²,S=1
def x(grid, tar):
    n = len(grid)
    for _ in range(4):
        for i in range(n):
            for j in range(i + 1, n):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
        for row in grid:
            row.reverse()
        if grid == tar:
            return True
    return False


for grid, tar in [
    ([[0, 1], [1, 0]], [[1, 0], [0, 1]]),
    ([[0, 1], [1, 1]], [[1, 0], [0, 1]]),
    ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]])
]:
    print(x(grid, tar))
