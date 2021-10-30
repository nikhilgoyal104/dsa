from collections import defaultdict


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, src, vis):
    vis.add(src)
    pre = [src]
    for nbr in graph[src]:
        if nbr not in vis:
            pre += dfs(graph, nbr, vis)
    return pre


def main(edges):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    cc, vis = [], set()
    for src in graph.keys():
        if src not in vis:
            cc.append(dfs(graph, src, vis))
    return cc, len(cc)


for edges in [
    [(0, 1), (2, 3), (4, 5), (4, 6), (5, 6)]
]:
    print(main(edges))
