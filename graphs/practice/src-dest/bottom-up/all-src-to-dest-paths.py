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
            return [[dest]]
        vis.add(src)
        res = []
        for nbr in graph[src]:
            if nbr not in vis:
                for path in dfs(nbr):
                    res.append([src] + path)
        vis.remove(src)
        return res

    return dfs(src)


for edges, data in inputs:
    for src, dest in data:
        print(main(edges, src, dest))

print()


def main(edges, src, dest):
    graph = build(edges)
    dp = {dest: [[dest]]}
    vis = set()

    def dfs(src):
        if src in dp:
            return dp[src]
        vis.add(src)
        dp[src] = []
        for nbr in graph[src]:
            if nbr not in vis:
                for path in dfs(nbr):
                    dp[src].append([src] + path)
        vis.remove(src)
        return dp[src]

    return dfs(src)


for edges, data in inputs:
    for src, dest in data:
        print(main(edges, src, dest))
