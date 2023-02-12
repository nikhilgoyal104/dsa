from collections import Counter


# T=mn,S=mn
def main(grid):
    m, n = len(grid), len(grid[0])
    gridClone = [[grid[ri][ci] for ci in range(n)] for ri in range(m)]
    offsets = (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)
    for ri in range(m):
        for ci in range(n):
            live = 0
            for x, y in offsets:
                if ri + x in [-1, m] or ci + y in [-1, n]:
                    continue
                if gridClone[ri + x][ci + y]:
                    live += 1
            if grid[ri][ci] and (live < 2 or live > 3):
                grid[ri][ci] = 0
            if not grid[ri][ci] and live == 3:
                grid[ri][ci] = 1
    return grid


for grid in [
    [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
    [[1, 1], [1, 0]]
]:
    print(main(grid))


# T=mn,S=1
def main(grid):
    m, n = len(grid), len(grid[0])
    offsets = (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)
    for ri in range(m):
        for ci in range(n):
            liveNeighbors = 0
            for x, y in offsets:
                if ri + x in [-1, m] or ci + y in [-1, n]:
                    continue
                if grid[ri + x][ci + y] in [1, 2]:
                    liveNeighbors += 1
            if grid[ri][ci] and (liveNeighbors < 2 or liveNeighbors > 3):
                grid[ri][ci] = 2
            if not grid[ri][ci] and liveNeighbors == 3:
                grid[ri][ci] = 3
    for i in range(m):
        for j in range(n):
            grid[i][j] %= 2
    return grid


for grid in [
    [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
    [[1, 1], [1, 0]]
]:
    print(main(grid))


def getCellsToComeAlive(currentLiveCells):
    liveNeighborFreq = Counter()
    for x, y in currentLiveCells:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                liveNeighborFreq[i, j] += 1
    cellsToComeAlive = set()
    for location, count in liveNeighborFreq.items():
        if count == 3 or (count == 2 and location in currentLiveCells):
            cellsToComeAlive.add(location)
    return cellsToComeAlive


def main(grid):
    m, n = len(grid), len(grid[0])
    currentLiveCells = {(i, j) for j in range(n) for i in range(m) if grid[i][j]}
    cellsToComeAlive = getCellsToComeAlive(currentLiveCells)
    for i in range(m):
        for j in range(n):
            grid[i][j] = int((i, j) in cellsToComeAlive)
    return grid


for grid in [
    [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
    [[1, 1], [1, 0]]
]:
    print(main(grid))
