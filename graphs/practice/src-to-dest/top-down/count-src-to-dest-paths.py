from collections import defaultdict


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def x(graph, src, dest):
    vis = set()

    def dfs(src):
        if src == dest:
            return 1
        vis.add(src)
        count = 0
        for nbr in graph[src]:
            if nbr not in vis:
                count += dfs(nbr)
        vis.remove(src)
        return count

    return dfs(src)


def y(graph, src, dest):
    dp, vis = {dest: 1}, set()

    def dfs(src):
        if src in dp:
            return dp[src]
        vis.add(src)
        dp[src] = 0
        for nbr in graph[src]:
            if nbr not in vis:
                dp[src] += dfs(nbr)
        vis.remove(src)
        return dp[src]

    return dfs(src)


def main(edges, src, dest):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    print(x(graph, src, dest), end=' ')
    print(y(graph, src, dest))


for edges, data in [
    ([(0, 1), (0, 3), (1, 2), (3, 2), (3, 4), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5)]),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)], [(0, 2), (2, 5)]),
]:
    [main(edges, src, dest) for src, dest in data]
    print()