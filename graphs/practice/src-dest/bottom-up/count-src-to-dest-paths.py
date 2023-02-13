from graphs.util import build

inputs = [
    ([(0, 1), (0, 3), (1, 2), (3, 2), (3, 4), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5)]),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)], [(0, 2), (2, 5)])
]


def main(edges, src, dest):
    graph = build(edges)
    vis = set()

    def dfs(src):
        if src == dest:
            return 1
        vis.add(src)
        res = 0
        for nbr in graph[src]:
            if nbr not in vis:
                res += dfs(nbr)
        vis.remove(src)
        return res

    return dfs(src)


for edges, data in inputs:
    for src, dest in data:
        print(main(edges, src, dest), end=' ')

print()


def main(edges, src, dest):
    graph = build(edges)
    dp = {dest: 1}
    vis = set()

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


for edges, data in inputs:
    for src, dest in data:
        print(main(edges, src, dest), end=' ')
