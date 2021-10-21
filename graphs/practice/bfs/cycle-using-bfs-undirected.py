from collections import defaultdict, deque


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph, src):
    queue = deque([(src, [src])])
    while queue:
        src, psf = queue.popleft()
        for nbr in graph[src]:
            if nbr not in psf:
                queue.append((nbr, psf + [nbr]))
            elif nbr != psf[-2]:
                return True
    return False


def main(edges):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    print(bfs(graph, 0))


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
]:
    main(edges)
