from collections import defaultdict


def construct(edges):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    return graph


def main(src, dest, edges):
    graph, vis = construct(edges), set()

    def dfs(src):
        if src == dest:
            return True
        vis.add(src)
        for nbr in graph[src]:
            if nbr not in vis and dfs(nbr):
                return True
        return False

    return dfs(src)


for src, dest, edges in [
    (0, 6, [(0, 1), (0, 3), (1, 2), (3, 2), (3, 4), (4, 5), (4, 6), (5, 6)]),
    (2, 5, [(0, 1), (0, 3), (1, 2), (3, 2), (3, 4), (4, 5), (4, 6), (5, 6)]),

    (0, 6, [(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)]),
    (2, 5, [(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)]),

    (0, 6, [(0, 1), (0, 3), (1, 2), (3, 2), (2, 5), (4, 5), (4, 6), (5, 6)]),
    (2, 5, [(0, 1), (0, 3), (1, 2), (3, 2), (2, 5), (4, 5), (4, 6), (5, 6)])
]:
    print(main(src, dest, edges))
