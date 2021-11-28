from graphs.util import build


def main(edges, src, dest):
    graph, vis = build(edges), set()

    def dfs(src):
        if src == dest:
            return [dest]
        vis.add(src)
        for nbr in graph[src]:
            if nbr not in vis:
                path = dfs(nbr)
                if path:
                    return [src] + path
        return []

    return dfs(src)


for edges, data in [
    ([(0, 1), (0, 3), (1, 2), (3, 2), (3, 4), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5)]),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)], [(0, 2), (2, 5)]),
]:
    for src, dest in data:
        print(main(edges, src, dest))
