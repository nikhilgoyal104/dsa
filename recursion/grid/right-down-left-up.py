from math import inf


def w(grid):
    m, n, vis = len(grid), len(grid[0]), set()

    def dfs(ri, ci):
        if ri in [-1, m] or ci in [-1, n] or (ri, ci) in vis:
            return 0
        if ri == m - 1 and ci == n - 1:
            return 1
        vis.add((ri, ci))
        count = 0
        for i, j in (0, 1), (1, 0), (-1, 0), (0, -1):
            count += dfs(ri + i, ci + j)
        vis.remove((ri, ci))
        return count

    return dfs(0, 0)


def x(grid):
    m, n, vis = len(grid), len(grid[0]), set()

    def dfs(ri, ci):
        if ri in [-1, m] or ci in [-1, n] or (ri, ci) in vis:
            return []
        if ri == m - 1 and ci == n - 1:
            return [[grid[-1][-1]]]
        if grid[ri][ci] == 10:
            return [[grid[ri][ci]]]
        vis.add((ri, ci))
        res = []
        for i, j in (0, 1), (1, 0), (-1, 0), (0, -1):
            for path in dfs(ri + i, ci + j):
                res.append([grid[ri][ci]] + path)
        vis.remove((ri, ci))
        return res

    return dfs(0, 0)


def y(grid):
    m, n, vis = len(grid), len(grid[0]), set()

    def dfs(ri, ci):
        if ri in [-1, m] or ci in [-1, n] or (ri, ci) in vis:
            return inf
        if ri == m - 1 and ci == n - 1:
            return 1
        vis.add((ri, ci))
        minimum = inf
        for i, j in (0, 1), (1, 0), (-1, 0), (0, -1):
            minimum = min(minimum, 1 + dfs(ri + i, ci + j))
        vis.remove((ri, ci))
        return minimum

    return dfs(0, 0)


def z(grid):
    m, n, vis = len(grid), len(grid[0]), set()

    def dfs(ri, ci):
        if ri in [-1, m] or ci in [-1, n] or (ri, ci) in vis:
            return inf
        if ri == m - 1 and ci == n - 1:
            return grid[-1][-1]
        vis.add((ri, ci))
        mcost = inf
        for i, j in (0, 1), (1, 0), (-1, 0), (0, -1):
            mcost = min(mcost, grid[ri][ci] + dfs(ri + i, ci + j))
        vis.remove((ri, ci))
        return mcost

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
