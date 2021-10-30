from collections import defaultdict


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def sdpaths(graph, src, dest, vis, path):
    if src == dest:
        print(path + [src], end=' ')
        return
    vis.add(src)
    path.append(src)
    for nbr in graph[src]:
        if nbr not in vis:
            sdpaths(graph, nbr, dest, vis, path)
    vis.remove(src)
    path.pop()


def main(edges, src, dest):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    sdpaths(graph, src, dest, set(), [])
    print()


for edges, data in [
    ([(0, 1), (0, 3), (1, 2), (3, 2), (3, 4), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5)]),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)], [(0, 2), (2, 5)]),
]:
    [main(edges, src, dest) for src, dest in data]
