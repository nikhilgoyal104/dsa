from collections import defaultdict


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def sdpaths(graph, src, dest, vis, psf):
    if src == dest:
        print(psf, end=' ')
        return
    [sdpaths(graph, nbr, dest, vis | {nbr}, psf + [nbr]) for nbr in graph[src] if nbr not in vis]


def main(edges, src, dest):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    sdpaths(graph, src, dest, {src}, [src])
    print()


for edges, data in [
    ([(0, 1), (0, 3), (1, 2), (3, 2), (3, 4), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5)]),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)], [(0, 2), (2, 5)]),
]:
    [main(edges, src, dest) for src, dest in data]
