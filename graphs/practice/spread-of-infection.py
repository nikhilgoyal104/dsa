from collections import defaultdict, deque
from graphs.util import build


def main(edges):
    res = 0
    graph = build(edges)
    queue = deque([(0, 0)])
    vis = {0}
    while queue:
        src, dist = queue.popleft()
        if dist == 2:
            break
        for nbr in graph[src]:
            if nbr not in vis:
                vis.add(nbr)
                queue.append((nbr, dist + 1))
                res += 1
    return res


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
]:
    print(main(edges))
