from collections import defaultdict
from graphs.util import build


def dfs(graph, src, vis):
    stack = [src]
    vis.add(src)
    while stack:
        src = stack.pop()
        print(src, end=' ')
        for nbr in reversed(graph[src]):
            if nbr not in vis:
                vis.add(nbr)
                stack.append(nbr)


def main(edges):
    graph, vis = build(edges), set()
    for src in graph:
        if src not in vis:
            dfs(graph, src, vis)
            print()
    print()


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
    [(0, 1), (2, 3), (4, 5), (4, 6), (5, 6)]
]:
    main(edges)
