from collections import defaultdict
from graphs.util import build6

inputs = [
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
]


def main(grid, src, dest):
    graph = build6(grid)
    vis = set()

    def dfs(src):
        if src == dest:
            return 0
        vis.add(src)
        res = float('inf')
        for nbr, cost in graph[src]:
            if nbr not in vis:
                res = min(res, cost + dfs(nbr))
        vis.remove(src)
        return res

    return dfs(src)


for grid, src, dest in inputs:
    print(main(grid, src, dest))

print()


def main(grid, src, dest):
    graph = build6(grid)
    cache = {dest: 0}
    vis = set()

    def dfs(src):
        if src in cache:
            return cache[src]
        vis.add(src)
        cache[src] = float('inf')
        for nbr, cost in graph[src]:
            if nbr not in vis:
                cache[src] = min(cache[src], cost + dfs(nbr))
        vis.remove(src)
        return cache[src]

    return dfs(src)


for grid, src, dest in inputs:
    print(main(grid, src, dest))
