from collections import defaultdict

inputs = [
    (7, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)]),
    (7, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]),
    (7, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]),
]


def construct(n, edges):
    graph = {i: [] for i in range(n)}
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    return graph


def main(n, edges):
    graph, vis = construct(n, edges), set()

    def dfs(src, parent):
        vis.add(src)
        for nbr in graph[src]:
            if nbr not in vis:
                if dfs(nbr, src):
                    return True
            elif nbr != parent:
                return True
        return False

    if dfs(0, -1):
        return False
    return len(vis) == n


for n, edges in inputs:
    print(main(n, edges))

print()


def main(n, edges):
    graph, vis = construct(n, edges), set()

    def dfs(src):
        vis.add(src)
        for nbr in graph[src]:
            if nbr not in vis:
                dfs(nbr)

    dfs(0)
    return len(vis) == n and len(edges) == n - 1


for n, edges in inputs:
    print(main(n, edges))
