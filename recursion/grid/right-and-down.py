def w(grid):
    m, n = len(grid), len(grid[0])
    cache = {(m - 1, n - 1): 1}

    def dfs(ri, ci):
        if ri == m or ci == n:
            return 0
        key = ri, ci
        if key in cache:
            return cache[key]
        cache[key] = 0
        for i, j in (0, 1), (1, 0):
            cache[key] += dfs(ri + i, ci + j)
        return cache[key]

    return dfs(0, 0)


def x(grid):
    m, n = len(grid), len(grid[0])
    cache = {(m - 1, n - 1): [[grid[-1][-1]]]}

    def dfs(ri, ci, vis):
        if ri in [-1, m] or ci in [-1, n] or (ri, ci) in vis:
            return []
        key = ri, ci
        if key in cache:
            return cache[key]
        vis.add((ri, ci))
        cache[key] = []
        for i, j in (0, 1), (1, 0):
            for path in dfs(ri + i, ci + j, vis):
                cache[key].append([grid[ri][ci]] + path)
        vis.remove((ri, ci))
        return cache[key]

    return dfs(0, 0, set())


def y(grid):
    m, n = len(grid), len(grid[0])
    cache = {(m - 1, n - 1): 1}

    def dfs(ri, ci):
        if ri == m or ci == n:
            return float('inf')
        key = ri, ci
        if key in cache:
            return cache[key]
        cache[key] = float('inf')
        for i, j in (0, 1), (1, 0):
            cache[key] = min(cache[key], 1 + dfs(ri + i, ci + j))
        return cache[key]

    return dfs(0, 0)


def z(grid):
    m, n = len(grid), len(grid[0])
    cache = {(m - 1, n - 1): grid[-1][-1]}

    def dfs(ri, ci):
        if ri == m or ci == n:
            return float('inf')
        key = ri, ci
        if key in cache:
            return cache[key]
        cache[key] = float('inf')
        for i, j in (0, 1), (1, 0):
            cache[key] = min(cache[key], grid[ri][ci] + dfs(ri + i, ci + j))
        return cache[key]

    return dfs(0, 0)


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
    ],
]:
    print(w(grid))
    print(x(grid))
    print(y(grid))
    print(z(grid))
    print()
