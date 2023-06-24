from collections import defaultdict
from graphs.util import build2


# T=v+e,S=v
def main(n, edges):
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

    return res


for n, edges in [
    (5, [[0, 1], [1, 2], [3, 4]]),
    (5, [[0, 1], [1, 2], [2, 3], [3, 4]])
]:
    print(main(n, edges))
