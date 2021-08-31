from collections import Counter


# T=mn,S=mn
def x(grid):
    m, n = len(grid), len(grid[0])
    gridc = [[grid[i][j] for j in range(n)] for i in range(m)]
    offsets = (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)
    for i in range(m):
        for j in range(n):
            live = 0
            for x, y in offsets:
                if i + x in [-1, m] or j + y in [-1, n]:
                    continue
                if gridc[i + x][j + y]:
                    live += 1
            if grid[i][j] and (live < 2 or live > 3):
                grid[i][j] = 0
            if not grid[i][j] and live == 3:
                grid[i][j] = 1
    return grid


for grid in [
    [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
    [[1, 1], [1, 0]]
]:
    print(x(grid))


# T=mn,S=1
def y(grid):
    m, n = len(grid), len(grid[0])
    offsets = (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)
    for i in range(m):
        for j in range(n):
            live = 0
            for x, y in offsets:
                if i + x in [-1, m] or j + y in [-1, n]:
                    continue
                if grid[i + x][j + y] in [1, 2]:
                    live += 1
            if grid[i][j] and (live < 2 or live > 3):
                grid[i][j] = 2
            if not grid[i][j] and live == 3:
                grid[i][j] = 3

    for i in range(m):
        for j in range(n):
            grid[i][j] %= 2

    return grid


for grid in [
    [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
    [[1, 1], [1, 0]]
]:
    print(y(grid))


def construct(live):
    freq = Counter()
    for x, y in live:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                freq[i, j] += 1
    return {ij for ij in freq if freq[ij] == 3 or (freq[ij] == 2 and ij in live)}


def z(grid):
    m, n = len(grid), len(grid[0])
    live = [(i, j) for j in range(n) for i in range(m) if grid[i][j]]
    live = construct(live)
    for i in range(m):
        for j in range(n):
            grid[i][j] = int((i, j) in live)
    return grid


for grid in [
    [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
    [[1, 1], [1, 0]]
]:
    print(z(grid))
