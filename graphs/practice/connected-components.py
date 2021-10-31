from graphs.util import build

edgesList = [
    [(0, 1), (2, 3), (4, 5), (4, 6), (5, 6)]
]


def main(edges):
    graph, vis = build(edges), set()
    res = []

    def dfs(src):
        vis.add(src)
        path.append(src)
        for nbr in graph[src]:
            if nbr not in vis:
                dfs(nbr)

    for src in graph:
        if src not in vis:
            path = []
            dfs(src)
            res.append(path)

    return res


for edges in edgesList:
    print(main(edges))
