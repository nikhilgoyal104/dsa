from collections import defaultdict, deque


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph, src, dest):
    queue = deque([(src, [src])])
    while queue:
        src, psf = queue.popleft()
        if src == dest:
            print(psf, end=' ')
            continue
        for nbr in graph[src]:
            if nbr not in psf:
                queue.append((nbr, psf + [nbr]))


def main(edges, src, dest):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    bfs(graph, src, dest)
    print()


for edges, data in [
    ([(0, 1), (0, 3), (1, 2), (3, 2), (3, 4), (4, 5), (4, 6), (5, 6)], [(0, 6), (2, 5)]),
    ([(0, 1), (0, 3), (1, 2), (3, 2), (4, 5), (4, 6), (5, 6)], [(0, 2), (2, 5)]),
]:
    [main(edges, src, dest) for src, dest in data]
