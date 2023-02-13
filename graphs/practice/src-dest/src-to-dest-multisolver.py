from collections import defaultdict
from graphs.util import build5
from heapq import *

heap = []
minLenPath = maxLenPath = shortestPath = longestPath = ceilPath = floorPath = None
shortestPathWeight = ceilPathWeight = float('inf')
longestPathWeight = floorPathWeight = float('-inf')


def main(edges, src, dest):
    graph = build5(edges)
    vis = set()
    k = 3

    def dfs(src, psf, wsf):
        global heap
        global minLenPath
        global maxLenPath
        global shortestPath
        global shortestPathWeight
        global longestPath
        global longestPathWeight
        global ceilPath
        global ceilPathWeight
        global floorPath
        global floorPathWeight
        if src == dest:
            if wsf < shortestPathWeight:
                shortestPathWeight, shortestPath = wsf, psf
            if wsf > longestPathWeight:
                longestPathWeight, longestPath = wsf, psf
            if 40 < wsf < ceilPathWeight:
                ceilPathWeight, ceilPath = wsf, psf
            if floorPathWeight < wsf < 40:
                floorPathWeight, floorPath = wsf, psf
            if len(heap) < k:
                heappush(heap, (wsf, psf))
            elif wsf > heap[0][0]:
                heappop(heap)
                heappush(heap, (wsf, psf))
            if not minLenPath or len(psf) < len(minLenPath):
                minLenPath = psf
            if not maxLenPath or len(psf) > len(maxLenPath):
                maxLenPath = psf
            return
        vis.add(src)
        for nbr, wt in graph[src]:
            if nbr not in vis:
                dfs(nbr, psf + [nbr], wsf + wt)
        vis.remove(src)

    dfs(src, [src], 0)


for edges, data in [
    ([(0, 1, 10), (0, 3, 40), (1, 2, 10), (3, 2, 10), (3, 4, 2), (4, 5, 3), (4, 6, 8), (5, 6, 3)], [(0, 6)])
]:
    for src, dest in data:
        main(edges, src, dest)
        print(str(shortestPath) + '@' + str(shortestPathWeight))
        print(str(longestPath) + '@' + str(longestPathWeight))
        print(str(ceilPath) + '@' + str(ceilPathWeight))
        print(str(floorPath) + '@' + str(floorPathWeight))
        kthPathWeight, kthPath = heap[0]
        print(str(kthPath) + '@' + str(kthPathWeight))
        print(minLenPath)
        print(maxLenPath)
