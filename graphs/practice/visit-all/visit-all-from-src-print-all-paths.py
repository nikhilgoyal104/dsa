from collections import defaultdict


def construct(edges):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    return graph


def main(edges, n):
    graph = construct(edges)
    path, vis = [], set()

    def dfs(src):
        if len(vis) == n - 1:
            print(path + [src])
            return
        vis.add(src)
        path.append(src)
        for nbr in graph[src]:
            if nbr not in vis:
                dfs(nbr)
        vis.remove(src)
        path.pop()

    dfs(0)


for edges, n in [
    ([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (2, 5), (4, 6)], 7),
    ([(0, 3), (3, 2), (2, 1), (0, 1), (3, 4), (4, 5), (4, 6), (5, 6)], 7)
]:
    main(edges, n)
    print()
