from collections import defaultdict, deque


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph, src, vis):
    queue = deque([src])
    vis.add(src)
    while queue:
        src = queue.popleft()
        print(src, end=' ')
        for nbr in graph[src]:
            if nbr not in vis:
                vis.add(nbr)
                queue.append(nbr)


def bfsl(graph, src, vis):
    queue = deque([src])
    vis.add(src)
    while queue:
        for _ in range(len(queue)):
            src = queue.popleft()
            print(src, end=' ')
            for nbr in graph[src]:
                if nbr not in vis:
                    vis.add(nbr)
                    queue.append(nbr)
        print()


def main(edges):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    vis = set()
    for src in graph.keys():
        if src not in vis:
            bfs(graph, src, vis)
            print()
    print()
    vis = set()
    for src in graph.keys():
        if src not in vis:
            bfsl(graph, src, vis)
            print()


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
    [(0, 1), (2, 3), (4, 5), (4, 6), (5, 6)]
]:
    main(edges)
