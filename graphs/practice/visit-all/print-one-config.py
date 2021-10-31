from collections import defaultdict
from graphs.util import build


def main(graph, n):
    graph = build(edges)
    path, vis = [], set()

    def dfs(src):
        vis.add(src)
        path.append(src)
        if len(vis) == n:
            return True
        for nbr in graph[src]:
            if nbr not in vis:
                if dfs(nbr):
                    return True
        vis.remove(src)
        path.pop()
        return False

    dfs(0)
    return path


for edges, n in [
    ([(0, 3), (3, 2), (2, 1), (0, 1), (3, 4), (4, 5), (4, 6), (5, 6)], 7)
]:
    print(main(edges, n))
