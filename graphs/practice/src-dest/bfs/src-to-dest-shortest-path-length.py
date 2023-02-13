from collections import defaultdict, deque
from graphs.util import build


def bfs(edges, src, dest):
    graph = build(edges)
    queue = deque([(src, 0)])
    vis = {src}
    while queue:
        src, dist = queue.popleft()
        if src == dest:
            return dist
        for nbr in graph[src]:
            if nbr not in vis:
                vis.add(nbr)
                queue.append((nbr, dist + 1))
    return -1


for edges, data in [
    ([(0, 1), (0, 3), (1, 2), (3, 2), (3, 4), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5)]),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)], [(0, 2), (2, 5)]),
]:
    for src, dest in data:
        print(bfs(edges, src, dest))
