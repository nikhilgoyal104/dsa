from collections import defaultdict, deque

edgesList = [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
    [(0, 1), (2, 3), (4, 5), (4, 6), (5, 6)]
]


def construct(edges):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    return graph


def main(edges):
    graph, vis = construct(edges), set()

    def bfs(src):
        queue = deque([src])
        vis.add(src)
        while queue:
            src = queue.popleft()
            print(src, end=' ')
            for nbr in graph[src]:
                if nbr not in vis:
                    vis.add(nbr)
                    queue.append(nbr)

    for src in graph:
        if src not in vis:
            bfs(src)


for edges in edgesList:
    main(edges)
    print()

print()


def main(edges):
    graph, vis = construct(edges), set()

    def bfs(src):
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

    for src in graph:
        if src not in vis:
            bfs(src)


for edges in edgesList:
    main(edges)
    print()
