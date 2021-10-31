from graphs.util import build


def sdpaths(graph, src, dest, vis, psf):
    if src == dest:
        print(psf, end=' ')
        return
    for nbr in graph[src]:
        if nbr not in vis:
            sdpaths(graph, nbr, dest, vis | {nbr}, psf + [nbr])


def main(edges, src, dest):
    graph = build(edges)
    sdpaths(graph, src, dest, {src}, [src])
    print()


for edges, data in [
    ([(0, 1), (0, 3), (1, 2), (3, 2), (3, 4), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5)]),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)], [(0, 2), (2, 5)]),
]:
    [main(edges, src, dest) for src, dest in data]
