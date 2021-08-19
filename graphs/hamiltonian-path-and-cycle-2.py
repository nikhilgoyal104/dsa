from collections import defaultdict

n = 7


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, src, vis, psf):
    if len(vis) == n - 1:
        return [psf + ['*']] if psf[-1] in graph[psf[0]] else [psf + ['.']]
    vis.add(src)
    res = []
    for nbr in graph[src]:
        if nbr not in vis:
            res += dfs(graph, nbr, vis, psf + [nbr])
    vis.remove(src)
    return res


def main(edges):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    print(dfs(graph, 0, set(), [0]))


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (2, 5), (4, 6)],
]:
    main(edges)
