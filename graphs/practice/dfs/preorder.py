from collections import defaultdict
from graphs.util import build


def main(edges):
    graph, vis = build(edges), set()
    res = []

    def dfs(src):
        vis.add(src)
        res = [src]
        for nbr in graph[src]:
            if nbr not in vis:
                res += dfs(nbr)
        return res

    for src in graph:
        if src not in vis:
            res.append(dfs(src))
    return res


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
    [(0, 1), (2, 3), (4, 5), (4, 6), (5, 6)]
]:
    print(main(edges))
