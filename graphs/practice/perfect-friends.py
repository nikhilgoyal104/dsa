from collections import defaultdict


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, src, vis):
    vis.add(src)
    count = 1
    for nbr in graph[src]:
        if nbr not in vis:
            count += dfs(graph, nbr, vis)
    return count


def main(edges):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    csl, vis = [], set()
    for src in graph.keys():
        if src not in vis:
            csl.append(dfs(graph, src, vis))
    return sum([csl[i] * sum(csl[i + 1:]) for i in range(len(csl))])


for edges in [
    [(0, 1), (2, 3), (4, 5), (5, 6), (4, 6)]
]:
    print(main(edges))
