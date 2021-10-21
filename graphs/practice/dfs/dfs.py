from collections import defaultdict


def construct(edges):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    return graph


def main(edges):
    graph, vis = construct(edges), set()

    def dfs(src):
        vis.add(src)
        print(src, end=' ')
        for nbr in graph[src]:
            if nbr not in vis:
                dfs(nbr)

    for src in graph:
        if src not in vis:
            dfs(src)
            print()


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
    [(0, 1), (2, 3), (4, 5), (4, 6), (5, 6)]
]:
    main(edges)
    print()
