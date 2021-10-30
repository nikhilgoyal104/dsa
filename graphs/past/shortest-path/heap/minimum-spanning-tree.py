from collections import defaultdict
from heapq import *


def add(graph, u, v, w, directed):
    graph[u].append((v, w))
    if not directed:
        graph[v].append((u, w))


def bfs(graph, src):
    heap, vis = [], set()
    heappush(heap, (0, src, -1))
    while heap:
        wt, src, parent = heappop(heap)
        if src in vis:
            continue
        vis.add(src)
        print(parent, src, wt)
        for nbr, wt in graph[src]:
            heappush(heap, (wt, nbr, src))


def main(edges, directed):
    graph = defaultdict(list)
    [add(graph, u, v, w, directed) for u, v, w in edges]
    bfs(graph, 0)
    print()


for edges, directed in [
    ([(0, 1, 10), (1, 2, 10), (2, 3, 10), (3, 4, 2), (4, 5, 3), (5, 6, 3), (0, 3, 40), (4, 6, 8)], False),
    ([(0, 1, 10), (1, 2, 10), (2, 3, 10), (3, 4, 2), (4, 5, 3), (5, 6, 3), (0, 3, 40), (4, 6, 8), (2, 5, 5)], False),
]:
    main(edges, directed)
