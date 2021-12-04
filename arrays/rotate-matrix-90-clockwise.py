# T=n²,S=1
def main(grid):
    n = len(grid)
    for i in range(n):
        for j in range(i + 1, n):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
    for i in range(n):
        low, high = 0, n - 1
        while low < high:
            grid[i][low], grid[i][high] = grid[i][high], grid[i][low]
            low, high = low + 1, high - 1
    for row in grid:
        print(row)


for grid in [
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
]:
    main(grid)
