from collections import defaultdict


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def path(graph, src, dest, vis):
    if src == dest:
        return True
    vis.add(src)
    for nbr in graph[src]:
        if nbr not in vis and path(graph, nbr, dest, vis):
            return True
    return False


def main(edges, src, dest):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    print(path(graph, src, dest, set()))


for edges, data in [
    ([(0, 1), (0, 3), (1, 2), (3, 2), (3, 4), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5)]),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5)]),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (2, 5), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5)]),
]:
    [main(edges, src, dest) for src, dest in data]
    print()
