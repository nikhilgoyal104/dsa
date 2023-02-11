from collections import defaultdict
from graphs.util import build


def odd(nbr, path):
    return nbr in path and (len(path) - path.index(nbr)) % 2 == 1


def main(edges):
    graph = build(edges)
    vis = set()
    path = []

    def dfs(src, parent):
        vis.add(src)
        path.append(src)
        for nbr in graph[src]:
            if nbr not in vis:
                if dfs(nbr, src):
                    return True
            elif nbr != parent and odd(nbr, path):
                return True
        path.pop()
        return False

    for src in graph:
        if src not in vis:
            if dfs(src, -1):
                return False

    return True


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3)],
    [(0, 1), (2, 3), (4, 5), (4, 6), (5, 6)],
]:
    print(main(edges))
