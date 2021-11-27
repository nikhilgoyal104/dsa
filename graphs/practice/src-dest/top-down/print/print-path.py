from collections import defaultdict


def build(edges, directed):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        if not directed:
            graph[dest].append(src)
    return graph


def main(edges, directed, src, dest):
    graph = build(edges, directed)
    path, vis = [], set()

    def dfs(src):
        path.append(src)
        if src == dest:
            return True
        vis.add(src)
        for nbr in graph[src]:
            if nbr not in vis:
                if dfs(nbr):
                    return True
        path.pop()
        return False

    dfs(src)
    return path


for edges, data, directed in [
    ([(0, 3), (3, 2), (2, 1), (0, 1), (3, 4), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5), (6, 2)], False),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)], [(0, 2), (2, 5)], False),
    ([(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (3, 8), (3, 9), (4, 10), (8, 11), (8, 12)], [(1, 11)], True),
]:
    for src, dest in data:
        print(main(edges, directed, src, dest))
