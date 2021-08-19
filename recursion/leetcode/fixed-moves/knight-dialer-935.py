import sys

sys.setrecursionlimit(550000)


# T=n,S=n
def x(length):
    dp, grid = {}, [[1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 1, 0]]
    m, n = 4, 3
    offsets = (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)

    def dfs(ri, ci, length):
        if ri < 0 or ri > m - 1 or ci < 0 or ci > n - 1 or not grid[ri][ci]:
            return 0
        if length == 1:
            return 1
        key = ri, ci, length
        if key in dp:
            return dp[key]
        dp[key] = 0
        for i, j in offsets:
            dp[key] += dfs(ri + i, ci + j, length - 1)
        return dp[key]

    return sum(dfs(i, j, length) for i in range(m) for j in range(n) if grid[i][j]) % (pow(10, 9) + 7)


# T=n,S=n
def y(length):
    graph = {
        1: (6, 8),
        2: (7, 9),
        3: (4, 8),
        4: (0, 3, 9),
        5: (),
        6: (0, 1, 7),
        7: (2, 6),
        8: (1, 3),
        9: (2, 4),
        0: (4, 6)
    }
    dp = {}

    def dfs(src, length):
        if length == 1:
            return 1
        key = src, length
        if key in dp:
            return dp[key]
        dp[key] = 0
        for nbr in graph[src]:
            dp[key] += dfs(nbr, length - 1)
        return dp[key]

    return sum(dfs(src, length) for src in graph) % (pow(10, 9) + 7)


for length in [1, 2, 3, 4, 3131, 4932, 4947]:
    print(x(length), end=' ')
    print(y(length))
