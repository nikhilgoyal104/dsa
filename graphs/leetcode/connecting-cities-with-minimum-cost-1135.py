from heapq import heappop, heappush

inputs = [
    (3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]),
    (4, [[1, 2, 3], [3, 4, 4]]),
    (4, [[1, 2, 1], [1, 3, 2], [3, 4, 4], [1, 4, 3]]),
    (5, [[2, 1, 50459], [3, 2, 47477], [4, 2, 52585], [5, 3, 16477]])
]


def build(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for src, dest, cost in edges:
        graph[src].append((dest, cost))
        graph[dest].append((src, cost))
    return graph


# T=nlogn,S=n
def main(n, connections):
    res, vis = 0, set()
    heap, graph = [], build(n, connections)
    heappush(heap, (0, 1))
    while heap:
        weight, src = heappop(heap)
        if src in vis:
            continue
        res += weight
        vis.add(src)
        for nbr, weight in graph[src]:
            if nbr not in vis:
                heappush(heap, (weight, nbr))
    return res if len(vis) == n else -1


for n, connections in inputs:
    print(main(n, connections))
