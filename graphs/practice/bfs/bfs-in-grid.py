from collections import deque


def outside(m, n, ri, ci):
    return ri in [-1, m] or ci in [-1, n]


def bfs(grid):
    m, n = len(grid), len(grid[0])
    queue, vis = deque([(0, 0)]), {(0, 0)}
    while queue:
        ri, ci = queue.popleft()
        print(grid[ri][ci], end=' ')
        for i, j in (-1, 0), (0, 1), (1, 0), (0, -1):
            if outside(m, n, ri + i, ci + j) or (ri + i, ci + j) in vis:
                continue
            vis.add((ri + i, ci + j))
            queue.append((ri + i, ci + j))


def bfsl(grid):
    m, n = len(grid), len(grid[0])
    queue, vis = deque([(0, 0)]), {(0, 0)}
    while queue:
        for _ in range(len(queue)):
            ri, ci = queue.popleft()
            print(grid[ri][ci], end=' ')
            for i, j in (-1, 0), (0, 1), (1, 0), (0, -1):
                if outside(m, n, ri + i, ci + j) or (ri + i, ci + j) in vis:
                    continue
                vis.add((ri + i, ci + j))
                queue.append((ri + i, ci + j))
        print()


def main(grid):
    bfs(grid)
    print()
    bfsl(grid)


for grid in [
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
]:
    main(grid)
