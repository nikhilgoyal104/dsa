def x(m, n):
    cache = {(m - 1, n - 1): 1}

    def dfs(ri, ci):
        if ri == m or ci == n:
            return 0
        key = ri, ci
        if key in cache:
            return cache[key]
        cache[key] = 0
        for i, j in (1, 0), (0, 1):
            cache[key] += dfs(ri + i, ci + j)
        return cache[key]

    return dfs(0, 0)


def y(m, n):
    cache = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
    return cache[-1][-1]


for m, n in [
    (3, 7),
    (3, 2),
    (7, 3),
    (3, 3)
]:
    print(x(m, n), end=' ')
    print(y(m, n))
