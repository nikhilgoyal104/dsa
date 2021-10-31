from graphs.util import build

n = 7


def dfs(graph, src, vis, psf):
    if len(vis) == n:
        return [psf + ['*']] if psf[-1] in graph[psf[0]] else [psf + ['.']]
    res = []
    for nbr in graph[src]:
        if nbr not in vis:
            res += dfs(graph, nbr, vis | {nbr}, psf + [nbr])
    return res


def main(edges):
    graph = build(edges)
    print(dfs(graph, 0, {0}, [0]))


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (2, 5), (4, 6)],
]:
    main(edges)
