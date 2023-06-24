from collections import defaultdict


def main(grid):
    graph = {i: [] for i in range(len(grid))}
    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            if grid[i][j]:
                graph[i].append(j)
                graph[j].append(i)

    vis = set()
    res = 0

    def dfs(src):
        vis.add(src)
        for nbr in graph[src]:
            if nbr not in vis:
                dfs(nbr)

    for src in graph:
        if src not in vis:
            dfs(src)
            res += 1

    return res


for grid in [
    [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ],
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
]:
    print(main(grid))
