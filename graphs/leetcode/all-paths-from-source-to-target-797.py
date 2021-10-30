graphs = [
    [[1, 2], [3], [3], []],
    [[4, 3, 1], [3, 2, 4], [3], [4], []],
    [[1], []],
    [[1, 2, 3], [2], [3], []],
    [[1, 3], [2], [3], []]
]


def main(graph):
    dest = len(graph) - 1

    def dfs(src):
        if src == dest:
            return [[dest]]
        res = []
        for nbr in graph[src]:
            for path in dfs(nbr):
                res.append([src] + path)
        return res

    return dfs(0)


for graph in graphs:
    print(main(graph))

print()


def main(graph):
    dest = len(graph) - 1
    dp = {dest: [[dest]]}

    def dfs(src):
        if src in dp:
            return dp[src]
        dp[src] = []
        for nbr in graph[src]:
            for path in dfs(nbr):
                dp[src].append([src] + path)
        return dp[src]

    return dfs(0)


for graph in graphs:
    print(main(graph))
