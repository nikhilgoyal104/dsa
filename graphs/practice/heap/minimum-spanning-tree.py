from heapq import heappush, heappop
from graphs.util import build4


# T=nlogn,S=n
def main(n, edges):
    res = 0
    graph = build4(n, edges)
    heap = []
    heappush(heap, (0, 0))
    vis = set()
    while heap:
        weight, src = heappop(heap)
        if src in vis:
            continue
        res += weight
        vis.add(src)
        for nbr, weight in graph[src]:
            if nbr not in vis:
                heappush(heap, (weight, nbr))
    return res if len(vis) == n else -1


for n, edges in [
    (7, [(0, 1, 10), (1, 2, 10), (2, 3, 10), (3, 4, 2), (4, 5, 3), (5, 6, 3), (0, 3, 40), (4, 6, 8)]),
    (7, [(0, 1, 10), (1, 2, 10), (2, 3, 10), (3, 4, 2), (4, 5, 3), (5, 6, 3), (0, 3, 40), (4, 6, 8), (2, 5, 5)]),
    (7, [(0, 1, 10), (1, 2, 10), (2, 3, 10), (3, 4, 2), (4, 5, 3)]),
]:
    print(main(n, edges))
