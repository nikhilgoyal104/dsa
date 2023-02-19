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
    cache = {dest: [[dest]]}

    def dfs(src):
        if src in cache:
            return cache[src]
        cache[src] = []
        for nbr in graph[src]:
            for path in dfs(nbr):
                cache[src].append([src] + path)
        return cache[src]

    return dfs(0)


for graph in graphs:
    print(main(graph))
