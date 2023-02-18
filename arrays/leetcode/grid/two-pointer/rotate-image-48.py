inputs = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ],
    [
        [1]
    ],
    [
        [1, 2],
        [3, 4]
    ]
]


# T=n²,S=1
def main(grid):
    n = len(grid)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = grid[n - j - 1][i]
    return res


for grid in inputs:
    print(main(grid))

print()


# T=n²,S=1
def main(grid):
    n = len(grid)
    for i in range(n):
        for j in range(i + 1, n):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
    for row in grid:
        row.reverse()


for grid in inputs:
    main(grid)
    print(grid)
