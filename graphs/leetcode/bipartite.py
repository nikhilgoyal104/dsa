from collections import defaultdict


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def odd(nbr, path):
    return nbr in path and (len(path) - path.index(nbr)) % 2 == 1


def dfs(graph, src, vis, parent, path):
    vis.add(src)
    path.append(src)
    for nbr in graph[src]:
        if nbr not in vis:
            if dfs(graph, nbr, vis, src, path):
                return True
        elif nbr != parent and odd(nbr, path):
            return True
    path.pop()
    return False


def main(edges):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    vis = set()
    for src in graph.keys():
        if src not in vis:
            if dfs(graph, src, vis, -1, []):
                return False
    return True


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3)],
    [(0, 1), (2, 3), (4, 5), (4, 6), (5, 6)],
]:
    print(main(edges))
