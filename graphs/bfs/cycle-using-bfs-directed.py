from collections import defaultdict, deque


def bfs(graph, src):
    queue, vis = deque([(src, [src])]), {src}
    while queue:
        src, psf = queue.popleft()
        for nbr in graph[src]:
            if nbr not in psf:
                queue.append((nbr, psf + [nbr]))
            else:
                return True
    return False


def main(n, edges):
    graph = defaultdict(list)
    for i in range(n):
        graph[i] = []
    [graph[u].append(v) for u, v in edges]
    print(bfs(graph, 0))


for n, edges in [
    (2, [(1, 0)]),
    (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 1)]),
    (5, [(0, 1), (1, 2), (2, 3), (3, 4), (1, 4)]),
]:
    main(n, edges)
