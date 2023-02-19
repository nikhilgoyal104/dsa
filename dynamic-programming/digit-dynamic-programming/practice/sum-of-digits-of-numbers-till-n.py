def x(n):
    n = str(n)
    size = len(n)

    def dfs(i, restrict, sum):
        if i == size:
            return sum
        res = 0
        limit = int(n[i]) if restrict else 9
        for digit in range(limit + 1):
            res += dfs(i + 1, False if digit < limit else restrict, sum + digit)
        return res

    return dfs(0, True, 0)


def y(n):
    n, cache = str(n), {}
    size = len(n)

    def dfs(i, restrict, sum):
        if i == size:
            return sum
        key = i, restrict, sum
        if key in cache:
            return cache[key]
        cache[key] = 0
        limit = int(n[i]) if restrict else 9
        for digit in range(limit + 1):
            cache[key] += dfs(i + 1, False if digit < limit else restrict, sum + digit)
        return cache[key]

    return dfs(0, True, 0)


for n in [
    10, 31, 48
]:
    print(x(n), end=' ')
    print(y(n))
