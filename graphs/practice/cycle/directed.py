from graphs.util import build3


# T=V+E,S=V
def main(n, edges):
    graph = build3(n, edges)
    vis = set()
    path = set()

    def dfs(src):
        vis.add(src)
        path.add(src)
        for nbr in graph[src]:
            if nbr in path:
                return True
            if nbr not in vis:
                if dfs(nbr):
                    return True
        path.remove(src)
        return False

    for src in range(n):
        if src not in vis:
            if dfs(src):
                return True
    return False


for n, edges in [
    (2, [(1, 0)]),
    (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 1)]),
    (5, [(0, 1), (1, 2), (2, 3), (3, 4), (1, 4)]),
    (10, [(0, 1), (2, 3), (3, 4), (4, 5), (6, 7), (7, 8), (8, 9), (9, 6)])
]:
    print(main(n, edges))
