# T=mn,S=1
def main(grid):
    res = []
    m, n = len(grid), len(grid[0])
    minRi = minCi = 0
    maxRi, maxCi = m - 1, n - 1
    while True:
        for ci in range(minCi, maxCi + 1):
            res.append(grid[minRi][ci])
        if len(res) == m * n:
            break
        minRi += 1
        for ri in range(minRi, maxRi + 1):
            res.append(grid[ri][maxCi])
        if len(res) == m * n:
            break
        maxCi -= 1
        for ci in range(maxCi, minCi - 1, -1):
            res.append(grid[maxRi][ci])
        if len(res) == m * n:
            break
        maxRi -= 1
        for ri in range(maxRi, minRi - 1, -1):
            res.append(grid[ri][minCi])
        if len(res) == m * n:
            break
        minCi += 1
    return res


for grid in [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
]:
    print(main(grid))
