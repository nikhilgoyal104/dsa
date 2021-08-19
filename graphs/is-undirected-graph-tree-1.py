from collections import defaultdict


def cyclic(graph, src, vis, parent):
    vis.add(src)
    for nbr in graph[src]:
        if nbr not in vis:
            if cyclic(graph, nbr, vis, src):
                return True
        elif nbr != parent:
            return True
    return False


def main(edges):
    n = 7
    graph = defaultdict(list)
    for i in range(n):
        graph[i] = []
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    vis = set()
    if cyclic(graph, 0, vis, -1):
        return False
    return len(vis) == n


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
]:
    print(main(edges))
