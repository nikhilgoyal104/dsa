def dfs(graph, src, vis, path):
    vis.add(src)
    for nbr in graph[src]:
        if nbr not in vis:
            dfs(graph, nbr, vis, path)
    path.append(src)


def main(n, edges):
    graph = {i: [] for i in range(n)}
    [graph[u].append(v) for u, v in edges]
    vis, path = set(), []
    for src in range(n):
        if src not in vis:
            dfs(graph, src, vis, path)
    path.reverse()
    print(path)


for n, edges in [
    (7, [(0, 1), (1, 2), (2, 3), (0, 3), (4, 5), (5, 6), (4, 6)]),
    (6, [(2, 3), (3, 1), (5, 2), (5, 0), (4, 0), (4, 1)])
]:
    main(n, edges)
