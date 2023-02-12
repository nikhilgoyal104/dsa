from heapq import heappush, heappop
from graphs.util import build4


def main(n, edges):
    res = 0
    graph = build4(n, edges)
    heap = []
    heappush(heap, (0, 0, [0]))
    vis = set()
    while heap:
        weightSoFar, src, pathSoFar = heappop(heap)
        if src in vis:
            continue
        vis.add(src)
        print(src, pathSoFar, weightSoFar)
        for nbr, weight in graph[src]:
            if nbr not in vis:
                heappush(heap, (weightSoFar + weight, nbr, pathSoFar + [nbr]))


for n, edges in [
    (7, [(0, 1, 10), (1, 2, 10), (2, 3, 10), (3, 4, 2), (4, 5, 3), (5, 6, 3), (0, 3, 40), (4, 6, 8)]),
    (7, [(0, 1, 10), (1, 2, 10), (2, 3, 10), (3, 4, 2), (4, 5, 3), (5, 6, 3), (0, 3, 40), (4, 6, 8), (2, 5, 5)])
]:
    main(n, edges)
    print()
