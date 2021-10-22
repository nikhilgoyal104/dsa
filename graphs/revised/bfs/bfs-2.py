from collections import defaultdict, deque


def construct(edges):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    return graph


def main(edges):
    graph, vis = construct(edges), set()
    queue = deque([0])
    while queue:
        src = queue.popleft()
        if src in vis:
            continue
        vis.add(src)
        print(src, end=' ')
        for nbr in graph[src]:
            queue.append(nbr)


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
]:
    main(edges)
