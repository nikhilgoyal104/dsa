from collections import deque


def outside(ri, ci, m, n):
    return ri in [-1, m] or ci in [-1, n]


def main(grid):
    m, n = len(grid), len(grid[0])
    fresh, rotten = 0, deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                fresh += 1
            elif grid[i][j] == 2:
                rotten.append((i, j))
    return 0 if not fresh else bfs(grid, fresh, rotten)


def bfs(grid, fresh, rotten):
    m, n, minutes = len(grid), len(grid[0]), 0
    while rotten:
        for _ in range(len(rotten)):
            ri, ci = rotten.popleft()
            for i, j in (-1, 0), (0, 1), (1, 0), (0, -1):
                if outside(ri + i, ci + j, m, n) or grid[ri + i][ci + j] in [0, 2]:
                    continue
                grid[ri + i][ci + j] = 2
                fresh -= 1
                rotten.append((ri + i, ci + j))
        minutes += 1
        if fresh == 0:
            break
    return minutes if not fresh else -1


for grid in [
    [[2, 1, 1], [1, 1, 0], [0, 1, 1]],
    [[2, 1, 1], [0, 1, 1], [1, 0, 1]],
    [[0, 2]]
]:
    print(main(grid))
