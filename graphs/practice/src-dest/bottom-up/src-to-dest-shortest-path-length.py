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
        res = float('inf')
        for nbr in graph[src]:
            if nbr not in vis:
                res = min(res, 1 + dfs(nbr))
        vis.remove(src)
        return res

    return dfs(src)


for edges, data in inputs:
    for src, dest in data:
        print(main(edges, src, dest))

print()


def main(edges, src, dest):
    graph = build(edges)
    cache = {dest: 1}
    vis = set()

    def dfs(src):
        if src in cache:
            return cache[src]
        vis.add(src)
        cache[src] = float('inf')
        for nbr in graph[src]:
            if nbr not in vis:
                cache[src] = min(cache[src], 1 + dfs(nbr))
        vis.remove(src)
        return cache[src]

    return dfs(src)


for edges, data in inputs:
    for src, dest in data:
        print(main(edges, src, dest))
