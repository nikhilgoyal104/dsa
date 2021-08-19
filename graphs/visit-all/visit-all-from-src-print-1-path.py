from collections import defaultdict

n = 7


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, src, vis, path):
    if len(vis) == n - 1:
        path.append(src)
        return True
    vis.add(src)
    path.append(src)
    for nbr in graph[src]:
        if nbr not in vis and dfs(graph, nbr, vis, path):
            return True
    vis.remove(src)
    path.pop()
    return False


def main(edges):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    path = []
    if dfs(graph, 0, set(), path):
        print(path)


for edges in [
    [(0, 3), (3, 2), (2, 1), (0, 1), (3, 4), (4, 5), (4, 6), (5, 6)]
]:
    main(edges)
