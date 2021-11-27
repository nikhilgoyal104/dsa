from math import inf


def construct(grid):
    graph = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                graph[i].append((j, grid[i][j]))
    return graph


def x(graph, src, dest):
    vis = set()

    def dfs(src):
        if src == dest:
            return 0
        vis.add(src)
        minimum = inf
        for nbr, cost in graph[src]:
            if nbr not in vis:
                minimum = min(minimum, cost + dfs(nbr))
        vis.remove(src)
        return minimum

    return dfs(src)


def y(graph, src, dest):
    dp, vis = {dest: 0}, set()

    def dfs(src):
        if src in dp:
            return dp[src]
        vis.add(src)
        dp[src] = inf
        for nbr, cost in graph[src]:
            if nbr not in vis:
                dp[src] = min(dp[src], cost + dfs(nbr))
        vis.remove(src)
        return dp[src]

    return dfs(src)


def main(grid, src, dest):
    grid = construct(grid)
    print(x(grid, src, dest), end=' ')
    print(y(grid, src, dest))


for grid, src, dest in [
    ([
         [0, -1, 0, 1, 0],
         [0, 0, -2, 0, 0],
         [-3, 0, 0, 0, 0],
         [0, 0, - 1, 0, 0],
         [0, 0, 0, 2, 0]
     ], 0, 2),
    ([
         [0, -7, 0, -2, 0],
         [0, 0, -11, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 3, -4],
         [0, 0, 0, 0, 0]
     ], 0, 4)
]:
    main(grid, src, dest)
