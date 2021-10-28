def main(n, edges):
    indegree, outdegree = [0] * n, [0] * n
    for src, dest in edges:
        outdegree[src] += 1
        indegree[dest] += 1
    return indegree, outdegree


for n, edges in [
    (2, [(1, 0)]),
    (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 1)]),
    (5, [(0, 1), (1, 2), (2, 3), (3, 4), (1, 4)]),
    (10, [(0, 1), (2, 3), (3, 4), (4, 5), (6, 7), (7, 8), (8, 9), (9, 6)])
]:
    print(main(n, edges))
