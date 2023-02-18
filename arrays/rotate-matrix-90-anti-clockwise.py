inputs = [
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
]


# T=n²,S=n²
def main(grid):
    n = len(grid)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = grid[j][n - i - 1]
    return res


for grid in inputs:
    print(main(grid))


# T=n²,S=1
def main(grid):
    n = len(grid)
    for i in range(n):
        for j in range(i + 1, n):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
    for i in range(n):
        low, high = 0, n - 1
        while low < high:
            grid[low][i], grid[high][i] = grid[high][i], grid[low][i]
            low, high = low + 1, high - 1


for grid in inputs:
    main(grid)
    print(grid)
