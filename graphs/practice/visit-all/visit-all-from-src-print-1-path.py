from collections import defaultdict


def construct(edges):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    return graph


def main(graph, n):
    graph = construct(edges)
    path, vis = [], set()

    def dfs(src):
        if len(vis) == n - 1:
            path.append(src)
            return True
        vis.add(src)
        path.append(src)
        for nbr in graph[src]:
            if nbr not in vis and dfs(nbr):
                return True
        vis.remove(src)
        path.pop()
        return False

    dfs(0)
    return path


for edges, n in [
    ([(0, 3), (3, 2), (2, 1), (0, 1), (3, 4), (4, 5), (4, 6), (5, 6)], 7)
]:
    print(main(edges, n))
