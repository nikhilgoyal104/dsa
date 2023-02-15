from collections import defaultdict
from graphs.util import build


def main(edges):
    graph = build(edges)
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

    return res


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
    [(0, 1), (2, 3), (4, 5), (4, 6), (5, 6)]
]:
    print(main(edges))
