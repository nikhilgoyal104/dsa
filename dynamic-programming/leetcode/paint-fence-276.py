def x(n, k):
    def dfs(i):
        if i == 1:
            return k
        if i == 2:
            return k * k
        return (k - 1) * (dfs(i - 1) + dfs(i - 2))

    return dfs(n)


# T=n,S=n
def y(n, k):
    cache = {1: k, 2: k * k}

    def dfs(i):
        if i in cache:
            return cache[i]
        cache[i] = (k - 1) * (dfs(i - 1) + dfs(i - 2))
        return cache[i]

    return dfs(n)


# T=n,S=n
def z(n, k):
    if n == 1:
        return k
    cache = [0] * n
    cache[0], cache[1] = k, k * k
    for i in range(2, n):
        cache[i] = (k - 1) * (cache[i - 1] + cache[i - 2])
    return cache[-1]


for n, k in [
    (4, 2),
    (3, 2),
    (1, 1),
    (7, 2),
]:
    print(x(n, k), end=' ')
    print(y(n, k), end=' ')
    print(z(n, k))
