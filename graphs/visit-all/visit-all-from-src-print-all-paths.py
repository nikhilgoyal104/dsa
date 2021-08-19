from collections import defaultdict

n = 7


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, src, vis, path):
    if len(vis) == n - 1:
        print(path + [src])
        return
    vis.add(src)
    path.append(src)
    [dfs(graph, nbr, vis, path) for nbr in graph[src] if nbr not in vis]
    vis.remove(src)
    path.pop()


def main(edges):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    dfs(graph, 0, set(), [])
    print()


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (2, 5), (4, 6)],
    [(0, 3), (3, 2), (2, 1), (0, 1), (3, 4), (4, 5), (4, 6), (5, 6)]

]:
    main(edges)
