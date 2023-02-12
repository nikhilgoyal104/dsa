from collections import defaultdict
from graphs.util import build


def main(edges):
    res = 0
    graph = build(edges)
    vis = set()

    def dfs(src):
        vis.add(src)
        res = 1
        for nbr in graph[src]:
            if nbr not in vis:
                res += dfs(nbr)
        return res

    count = []
    for src in graph:
        if src not in vis:
            count.append(dfs(src))
    for i in range(len(count)):
        res += count[i] * sum(count[i + 1:])
    return res


for edges in [
    [(0, 1), (2, 3), (4, 5), (5, 6), (4, 6)]
]:
    print(main(edges))
