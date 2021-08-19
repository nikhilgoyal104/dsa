from collections import defaultdict, deque


def add(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph, src):
    queue, vis, count = deque([(src, 0)]), {src}, 1
    while queue:
        src, dist = queue.popleft()
        print(src, end=' ')
        if dist == 2:
            break
        for nbr in graph[src]:
            if nbr not in vis:
                vis.add(nbr)
                queue.append((nbr, dist + 1))
                count += 1
    print()
    return count


def main(edges):
    graph = defaultdict(list)
    [add(graph, u, v) for u, v in edges]
    print(bfs(graph, 6))


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
]:
    main(edges)
