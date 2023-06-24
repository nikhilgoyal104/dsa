from collections import defaultdict
from graphs.util import build2


def main(n, edges):
    if len(edges) < n - 1:
        return -1
    graph = build2(n, edges)
    vis = set()
    res = 0

    def dfs(src):
        vis.add(src)
        for nbr in graph[src]:
            if nbr not in vis:
                dfs(nbr)

    for src in graph:
        if src not in vis:
            dfs(src)
            res += 1

    return res - 1


for n, edges in [
    (4, [[0, 1], [0, 2], [1, 2]]),
    (6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]),
    (6, [[0, 1], [0, 2], [0, 3], [1, 2]])
]:
    print(main(n, edges))
