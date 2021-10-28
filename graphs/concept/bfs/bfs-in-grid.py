from collections import deque

grids = [
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
]


def outside(m, n, nbr):
    return nbr[0] in [-1, m] or nbr[1] in [-1, n]


def main(grid):
    m, n = len(grid), len(grid[0])
    offsets = (0, 1), (1, 0), (0, -1), (-1, 0)
    queue, vis = deque([(0, 0)]), {(0, 0)}
    while queue:
        ri, ci = queue.popleft()
        print(grid[ri][ci], end=' ')
        for i, j in offsets:
            nbr = ri + i, ci + j
            if outside(m, n, nbr) or nbr in vis:
                continue
            vis.add(nbr)
            queue.append(nbr)


for grid in grids:
    main(grid)
    print()

print()


def main(grid):
    m, n = len(grid), len(grid[0])
    offsets = (0, 1), (1, 0), (0, -1), (-1, 0)
    queue, vis = deque([(0, 0)]), {(0, 0)}
    while queue:
        for _ in range(len(queue)):
            ri, ci = queue.popleft()
            print(grid[ri][ci], end=' ')
            for i, j in offsets:
                nbr = ri + i, ci + j
                if outside(m, n, nbr) or nbr in vis:
                    continue
                vis.add(nbr)
                queue.append(nbr)
        print()


for grid in grids:
    main(grid)
    print()
