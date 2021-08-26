def main(n, edges):
    indegrees, outdegrees = [0] * n, [0] * n
    for u, v in edges:
        outdegrees[u] += 1
        indegrees[v] += 1
    print('ind->' + str(indegrees))
    print('out->' + str(outdegrees))


for n, edges in [
    (2, [(1, 0)]),
    (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 1)]),
    (5, [(0, 1), (1, 2), (2, 3), (3, 4), (1, 4)]),
    (10, [(0, 1), (2, 3), (3, 4), (4, 5), (6, 7), (7, 8), (8, 9), (9, 6)])
]:
    main(n, edges)
    print()
