from collections import defaultdict, deque
from math import inf
from pprint import pprint


def add(graph, u, v, w, directed):
    graph[u].append((v, w))
    if not directed:
        graph[v].append((u, w))


def bfs(graph, src):
    queue, mwt, spath = deque([(src, [src])]), defaultdict(lambda: inf), defaultdict(list)
    mwt[src] = 0
    while queue:
        src, psf = queue.popleft()
        for nbr, wt in graph[src]:
            if nbr not in psf:
                queue.append((nbr, psf + [nbr]))
                if mwt[src] + wt < mwt[nbr]:
                    spath[nbr] = psf + [nbr]
                    mwt[nbr] = mwt[src] + wt
    pprint(dict(spath))
    return mwt


def main(edges, directed):
    graph = defaultdict(list)
    [add(graph, u, v, w, directed) for u, v, w in edges]
    pprint(dict(bfs(graph, 0)), width=1)


for edges, directed in [
    ([(0, 1, 10), (1, 2, 10), (2, 3, 10), (3, 4, 2), (4, 5, 3), (5, 6, 3), (0, 3, 40), (4, 6, 8)], False),
    ([(0, 1, 10), (1, 2, 10), (2, 3, 10), (3, 4, 2), (4, 5, 3), (5, 6, 3), (0, 3, 40), (4, 6, 8), (2, 5, 5)], False),
    ([(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)], True)
]:
    main(edges, directed)
