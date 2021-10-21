from collections import defaultdict, deque


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph, src):
    queue, vis = deque([src]), set()
    while queue:
        src = queue.popleft()
        if src in vis:
            continue
        vis.add(src)
        print(src, end=' ')
        for nbr in graph[src]:
            queue.append(nbr)


def main(edges):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    bfs(graph, 0)


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
]:
    main(edges)
