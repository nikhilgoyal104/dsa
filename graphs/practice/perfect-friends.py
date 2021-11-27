from collections import defaultdict
from graphs.util import build


def main(edges):
    graph, vis = build(edges), set()

    def dfs(src):
        vis.add(src)
        res = 1
        for nbr in graph[src]:
            if nbr not in vis:
                res += dfs(nbr)
        return res

    countPerClub = []
    for src in graph:
        if src not in vis:
            countPerClub.append(dfs(src))
    res = 0
    for i in range(len(countPerClub)):
        res += countPerClub[i] * sum(countPerClub[i + 1:])
    return res


for edges in [
    [(0, 1), (2, 3), (4, 5), (5, 6), (4, 6)]
]:
    print(main(edges))
