from collections import defaultdict
from graphs.util import build


def dfs(graph, src, vis):
    vis.add(src)
    for nbr in graph[src]:
        if nbr not in vis:
            dfs(graph, nbr, vis)


def main(edges):
    graph, vis = build(edges), set()
    dfs(graph, 0, vis)
    return len(vis) == len(graph.keys())


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
    [(0, 1), (2, 3), (4, 5), (4, 6), (5, 6)]
]:
    print(main(edges))
