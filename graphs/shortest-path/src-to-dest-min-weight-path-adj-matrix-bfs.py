from collections import defaultdict, deque
from math import inf


def bfs(graph, src, dest):
    queue, mwt = deque([(src, [src])]), defaultdict(lambda: inf)
    mwt[src] = 0
    while queue:
        src, psf = queue.popleft()
        if src == dest:
            continue
        for nbr, wt in graph[src]:
            if nbr not in psf:
                queue.append((nbr, psf + [nbr]))
                mwt[nbr] = min(mwt[nbr], mwt[src] + wt)
    return mwt[dest]


def main(grid, src, dest):
    graph = defaultdict(list)
    [graph[i].append((j, grid[i][j])) for j in range(len(grid[0])) for i in range(len(grid)) if grid[i][j]]
    print(bfs(graph, src, dest))


for grid, src, dest in [
    ([
         [0, -1, 0, 1, 0],
         [0, 0, -2, 0, 0],
         [-3, 0, 0, 0, 0],
         [0, 0, - 1, 0, 0],
         [0, 0, 0, 2, 0]
     ], 0, 2),
    ([
         [0, -7, 0, -2, 0],
         [0, 0, -11, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 3, -4],
         [0, 0, 0, 0, 0]
     ], 0, 4)
]:
    main(grid, src, dest)
