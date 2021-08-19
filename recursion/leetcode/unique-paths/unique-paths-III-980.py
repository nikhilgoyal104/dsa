def construct(grid):
    m, n = len(grid), len(grid[0])
    sri, sci, nonObstacleCount = 0, 0, 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                sri, sci = i, j
                nonObstacleCount += 1
            elif grid[i][j] in [0, 2]:
                nonObstacleCount += 1
    return sri, sci, nonObstacleCount


# T=3ⁿ,S=n
def x(grid):
    m, n, vis = len(grid), len(grid[0]), set()
    sri, sci, nonObstacleCount = construct(grid)

    def dfs(ri, ci):
        if ri in [-1, m] or ci in [-1, n] or grid[ri][ci] == -1 or (ri, ci) in vis:
            return 0
        if grid[ri][ci] == 2:
            return 1 if len(vis) == nonObstacleCount - 1 else 0
        vis.add((ri, ci))
        count = 0
        for i, j in (1, 0), (0, 1), (-1, 0), (0, -1):
            count += dfs(ri + i, ci + j)
        vis.remove((ri, ci))
        return count

    return dfs(sri, sci)


for grid in [
    [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]],
    [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]],
    [[0, 1], [2, 0]]
]:
    print(x(grid))
