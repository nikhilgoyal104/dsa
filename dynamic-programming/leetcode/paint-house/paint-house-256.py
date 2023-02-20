# T=kⁿ,S=k
def x(grid):
    m, n = len(grid), len(grid[0])

    def dfs(ri, ci):
        if ri == m - 1:
            return grid[ri][ci]
        res = float('inf')
        for j in range(n):
            if j != ci:
                res = min(res, grid[ri][ci] + dfs(ri + 1, j))
        return res

    return min(dfs(0, j) for j in range(n))


# T=nk²,S=nk
def y(grid):
    m, n = len(grid), len(grid[0])
    cache = {}

    def dfs(ri, ci):
        if ri == m - 1:
            return grid[ri][ci]
        key = ri, ci
        if key in cache:
            return cache[key]
        cache[key] = float('inf')
        for j in range(n):
            if j != ci:
                cache[key] = min(cache[key], grid[ri][ci] + dfs(ri + 1, j))
        return cache[key]

    return min(dfs(0, j) for j in range(n))


# T=nk²,S=nk
def z(grid):
    m, n = len(grid), len(grid[0])
    cache = [[0] * n for _ in range(m)]
    for j in range(n):
        cache[0][j] = grid[0][j]
    for i in range(1, m):
        for j in range(n):
            cache[i][j] = grid[i][j] + min(cache[i - 1][:j] + cache[i - 1][j + 1:])
    return min(cache[-1])


for grid in [
    [
        [1, 5, 7],
        [5, 8, 4],
        [3, 2, 9],
        [1, 2, 4]
    ],
    [
        [17, 2, 17],
        [16, 16, 5],
        [14, 3, 19]
    ],
    [
        [7, 6, 2]
    ]
]:
    print(x(grid), end=' ')
    print(y(grid), end=' ')
    print(z(grid))
