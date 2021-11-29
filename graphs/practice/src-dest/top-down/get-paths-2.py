from graphs.util import build


def main(edges, src, dest):
    graph = build(edges)
    path, vis = [], set()

    def dfs(src):
        if src == dest:
            return [path + [src]]
        path.append(src)
        vis.add(src)
        res = []
        for nbr in graph[src]:
            if nbr not in vis:
                res += dfs(nbr)
        vis.remove(src)
        path.pop()
        return res

    return dfs(src)


for edges, data in [
    ([(0, 1), (0, 3), (1, 2), (3, 2), (3, 4), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5)]),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)], [(0, 2), (2, 5)]),
]:
    for src, dest in data:
        print(main(edges, src, dest))
