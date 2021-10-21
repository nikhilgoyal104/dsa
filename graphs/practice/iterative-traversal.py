from collections import defaultdict


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, src, vis):
    stack = [src]
    vis.add(src)
    while stack:
        src = stack.pop()
        print(src, end=' ')
        for nbr in reversed(graph[src]):
            if nbr not in vis:
                vis.add(nbr)
                stack.append(nbr)


def main(edges):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    vis = set()
    for src in graph.keys():
        if src not in vis:
            dfs(graph, src, vis)
            print()
    print()


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
    [(0, 1), (2, 3), (4, 5), (4, 6), (5, 6)]
]:
    main(edges)
