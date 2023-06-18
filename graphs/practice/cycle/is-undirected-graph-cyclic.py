from collections import defaultdict
from graphs.util import build2


# T=V+E,S=V
def main(n, edges):
    graph = build2(n, edges)
    vis = set()

    def dfs(src, parent):
        vis.add(src)
        for nbr in graph[src]:
            if nbr not in vis:
                if dfs(nbr, src):
                    return True
            elif nbr != parent:
                return True
        return False

    for src in graph:
        if src not in vis:
            if dfs(src, -1):
                return True

    return False


for n, edges in [
    (7, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)]),
    (7, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]),
    (7, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]),
]:
    print(main(n, edges))
