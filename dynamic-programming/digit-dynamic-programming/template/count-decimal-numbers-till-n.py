def x(n):
    n = str(n)
    size = len(n)

    def dfs(i, restrict):
        if i == size:
            return 1
        count, limit = 0, int(n[i]) if restrict else 9
        for digit in range(limit + 1):
            count += dfs(i + 1, False if digit < limit else restrict)
        return count

    return dfs(0, True)


def y(n):
    n, cache = str(n), {}
    size = len(n)

    def dfs(i, restrict):
        if i == size:
            return 1
        key = i, restrict
        if key in cache:
            return cache[key]
        cache[key], limit = 0, int(n[i]) if restrict else 9
        for digit in range(limit + 1):
            cache[key] += dfs(i + 1, False if digit < limit else restrict)
        return cache[key]

    return dfs(0, True)


for n in [42, 149]:
    print(x(n), end=' ')
    print(y(n))
