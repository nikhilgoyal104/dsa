from graphs.util import build2


def main(n, edges):
    graph = build2(n, edges)
    vis = set()

    def dfs(src):
        vis.add(src)
        if len(vis) == n:
            vis.remove(src)
            return [[src]]
        res = []
        for nbr in graph[src]:
            if nbr not in vis:
                for path in dfs(nbr):
                    res.append([src] + path)
        vis.remove(src)
        return res

    res = dfs(0)
    for path in res:
        if path[-1] in graph[path[0]]:
            path.append('*')
        else:
            path.append('.')
    return res


for n, edges in [
    (7, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (2, 5), (4, 6)]),
]:
    print(main(n, edges))
