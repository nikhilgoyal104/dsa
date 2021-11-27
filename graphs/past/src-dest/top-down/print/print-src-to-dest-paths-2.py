from graphs.util import build


def main(edges, src, dest):
    graph = build(edges)

    def dfs(src, vis, path):
        if src == dest:
            print(path, end=' ')
            return
        for nbr in graph[src]:
            if nbr not in vis:
                dfs(nbr, vis | {nbr}, path + [nbr])

    dfs(src, {src}, [src])


for edges, data in [
    ([(0, 1), (0, 3), (1, 2), (3, 2), (3, 4), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5)]),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)], [(0, 2), (2, 5)]),
]:
    for src, dest in data:
        main(edges, src, dest)
        print()
