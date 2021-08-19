from collections import defaultdict


def dfs(graph, src, vis):
    vis.add(src)
    [dfs(graph, nbr, vis) for nbr in graph[src] if nbr not in vis]


def main(edges):
    n = 7
    graph = defaultdict(list)
    for i in range(n):
        graph[i] = []
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    vis = set()
    dfs(graph, 0, vis)
    return len(vis) == n and len(edges) == n - 1


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
]:
    print(main(edges))
