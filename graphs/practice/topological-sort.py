def construct(n, edges):
    graph = {i: [] for i in range(n)}
    for src, dest in edges:
        graph[src].append(dest)
    return graph


def main(n, edges):
    graph = construct(n, edges)
    path, vis = [], set()

    def dfs(src):
        vis.add(src)
        for nbr in graph[src]:
            if nbr not in vis:
                dfs(nbr)
        path.append(src)

    for src in graph:
        if src not in vis:
            dfs(src)

    path.reverse()
    return path


for n, edges in [
    (7, [(0, 1), (1, 2), (2, 3), (0, 3), (4, 5), (5, 6), (4, 6)]),
    (6, [(2, 3), (3, 1), (5, 2), (5, 0), (4, 0), (4, 1)])
]:
    print(main(n, edges))
