def getFirstAndSecondMin(row):
    firstMin = secondMin = float('inf')
    for val in row:
        if val < firstMin:
            secondMin = firstMin
            firstMin = val
        elif val < firstMin:
            secondMin = val
    return firstMin, secondMin


# T=nk,S=nk
def main(grid):
    m, n = len(grid), len(grid[0])
    cache = [[0] * n for _ in range(m)]
    for j in range(n):
        cache[0][j] = grid[0][j]
    firstMin, secondMin = getFirstAndSecondMin(cache[0])
    for i in range(1, m):
        for j in range(n):
            cache[i][j] = grid[i][j] + (firstMin if cache[i - 1][j] != firstMin else secondMin)
        firstMin, secondMin = getFirstAndSecondMin(cache[i])
    return min(cache[-1])


for grid in [
    [
        [1, 5, 3],
        [2, 9, 4]
    ],
    [
        [1, 3], [2, 4]
    ],
    [
        [10, 6, 16, 25, 7, 28],
        [7, 16, 18, 30, 16, 25],
        [8, 26, 6, 22, 26, 19],
        [10, 23, 14, 17, 23, 9],
        [12, 14, 27, 7, 8, 9]
    ]
]:
    print(main(grid))
