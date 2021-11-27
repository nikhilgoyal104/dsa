from collections import defaultdict
from heapq import *


def add(graph, u, v, wt):
    graph[u].append((v, wt))
    graph[v].append((u, wt))


minlenpath, maxlenpath = [], []
spath, spathwt = None, float('inf')
lpath, lpathwt = None, float('-inf')
cpath, cpathwt = None, float('inf')
fpath, fpathwt = None, float('-inf')
pq, k = [], 3


def sdpath(graph, src, dest, vis, psf, wsf):
    global spath, spathwt, lpath, lpathwt, cpath, cpathwt, fpath, fpathwt, minlenpath, maxlenpath, k, pq
    if src == dest:
        if wsf < spathwt:
            spathwt, spath = wsf, psf
        if wsf > lpathwt:
            lpathwt, lpath = wsf, psf
        if 40 < wsf < cpathwt:
            cpathwt, cpath = wsf, psf
        if fpathwt < wsf < 40:
            fpathwt, fpath = wsf, psf
        if len(pq) < 3:
            heappush(pq, (wsf, psf))
        elif wsf > pq[0][0]:
            heappop(pq)
            heappush(pq, (wsf, psf))
        if not minlenpath or len(psf) < len(minlenpath):
            minlenpath = psf
        if not maxlenpath or len(psf) > len(maxlenpath):
            maxlenpath = psf
        return
    vis.add(src)
    for nbr, wt in graph[src]:
        if nbr not in vis:
            sdpath(graph, nbr, dest, vis, psf + [nbr], wsf + wt)
    vis.remove(src)


def main(edges, src, dest):
    graph = defaultdict(list)
    [add(graph, u, v, wt) for u, v, wt in edges]
    sdpath(graph, src, dest, set(), [src], 0)
    print(str(spath) + '@' + str(spathwt))
    print(str(lpath) + '@' + str(lpathwt))
    print(str(cpath) + '@' + str(cpathwt))
    print(str(fpath) + '@' + str(fpathwt))
    kpathwt, kpath = pq[0]
    print(str(kpath) + '@' + str(kpathwt))
    print(minlenpath)
    print(maxlenpath)


for edges, data in [
    ([(0, 1, 10), (0, 3, 40), (1, 2, 10), (3, 2, 10), (3, 4, 2), (4, 5, 3), (4, 6, 8), (5, 6, 3)], [(0, 6)]),
]:
    [main(edges, src, dest) for src, dest in data]
    print()
