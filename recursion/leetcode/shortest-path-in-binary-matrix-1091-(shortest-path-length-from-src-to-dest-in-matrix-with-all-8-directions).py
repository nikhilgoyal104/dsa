from math import inf
from collections import deque


# T=8ᵐⁿ,S=mn
def main(grid):
    m, n = len(grid), len(grid[0])
    offsets = (0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)

    def dfs(ri, ci, vis):
        if ri in [-1, m] or ci in [-1, n] or (ri, ci) in vis or grid[ri][ci] == 1:
            return inf
        if ri == m - 1 and ci == n - 1:
            return 1
        vis.add((ri, ci))
        res = inf
        for i, j in offsets:
            res = min(res, 1 + dfs(ri + i, ci + j, vis))
        vis.remove((ri, ci))
        return res

    res = dfs(0, 0, set())
    return -1 if res == inf else res


for grid in [
    [[0, 1], [1, 0]],
    [[0, 0, 0], [1, 1, 0], [1, 1, 0]],
    [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
]:
    print(main(grid), end=' ')

print()


# T=m+n,S=m+n
def x(grid):
    if grid[0][0] == 1:
        return -1
    m, n = len(grid), len(grid[0])
    queue, vis = deque([(0, 0, 1)]), {(0, 0)}
    while queue:
        ri, ci, dist = queue.popleft()
        if (ri, ci) == (m - 1, n - 1):
            return dist
        for i, j in (0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1):
            x, y = ri + i, ci + j
            if (x, y) in vis or x in [-1, m] or y in [-1, n] or grid[x][y]:
                continue
            vis.add((x, y))
            queue.append((x, y, dist + 1))
    return -1


# T=m+n,S=m+n
def y(grid):
    if grid[0][0] == 1:
        return -1
    m, n = len(grid), len(grid[0])
    queue = deque([(0, 0, 1)])
    grid[0][0] = 1
    while queue:
        ri, ci, dist = queue.popleft()
        if (ri, ci) == (m - 1, n - 1):
            return dist
        for i, j in (0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1):
            x, y = ri + i, ci + j
            if x in [-1, m] or y in [-1, n] or grid[x][y]:
                continue
            grid[x][y] = 1
            queue.append((x, y, dist + 1))
    return -1


for grid in [
    [[0, 1], [1, 0]],
    [[0, 0, 0], [1, 1, 0], [1, 1, 0]],
    [[1, 0, 0], [1, 1, 0], [1, 1, 0]],
    [[0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1], [1, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0]]
]:
    print(x(grid), end=' ')
    print(y(grid))
