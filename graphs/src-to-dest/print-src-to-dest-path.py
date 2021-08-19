from collections import defaultdict


def add(graph, u, v, directed):
    graph[u].append(v)
    if not directed:
        graph[v].append(u)


def sdpath(graph, src, dest, vis, path):
    if src == dest:
        return True
    vis.add(src)
    path.append(src)
    for nbr in graph[src]:
        if nbr not in vis and sdpath(graph, nbr, dest, vis, path):
            return True
    path.pop()
    return False


def main(edges, directed, src, dest):
    graph = defaultdict(list)
    [add(graph, u, v, directed) for u, v in edges]
    path = []
    if sdpath(graph, src, dest, set(), path):
        print(path + [dest])
    else:
        print([])


for edges, data, directed in [
    ([(0, 3), (3, 2), (2, 1), (0, 1), (3, 4), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5), (6, 2)], False),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)], [(0, 2), (2, 5)], False),
    ([(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (3, 8), (3, 9), (4, 10), (8, 11), (8, 12)], [(1, 11)], True),
]:
    [main(edges, directed, src, dest) for src, dest in data]
    print()
