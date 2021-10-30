from collections import defaultdict, deque


def construct(edges):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    return graph


def main(edges):
    graph, vis = construct(edges), {0}
    queue, res = deque([(0, 0)]), [[], 1]
    while queue:
        src, dist = queue.popleft()
        res[0].append(src)
        if dist == 2:
            break
        for nbr in graph[src]:
            if nbr not in vis:
                vis.add(nbr)
                queue.append((nbr, dist + 1))
                res[1] += 1
    return res


for edges in [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 3), (4, 6)],
]:
    print(main(edges))
