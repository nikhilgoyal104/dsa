from collections import deque


def main(n, edges):
    graph, indegree = {i: [] for i in range(n)}, [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    queue, ts, levels = deque(), [], 0
    [queue.append(i) for i, v in enumerate(indegree) if v == 0]
    while queue:
        for _ in range(len(queue)):
            src = queue.popleft()
            ts.append(src)
            for nbr in graph[src]:
                indegree[nbr] -= 1
                if not indegree[nbr]:
                    queue.append(nbr)
        levels += 1
    print(ts, levels)


for n, edges in [
    (7, [(0, 1), (1, 2), (2, 3), (0, 3), (4, 5), (5, 6), (4, 6)]),
    (6, [(2, 3), (3, 1), (5, 2), (5, 0), (4, 0), (4, 1)])
]:
    main(n, edges)
