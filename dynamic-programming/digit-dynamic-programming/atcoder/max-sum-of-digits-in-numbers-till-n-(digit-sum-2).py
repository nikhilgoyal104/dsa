def total(n):
    return sum(int(digit) for digit in n)


def x(n):
    n = str(n)
    size = len(n)
    return max(total(str(int(n[0]) - 1) + (size - 1) * '9'), total(n))


def y(n):
    n, cache = str(n), {}
    size = len(n)

    def dfs(i, restrict, sum):
        if i == size:
            return sum
        key = i, restrict, sum
        if key in cache:
            return cache[key]
        cache[key], limit = 0, int(n[i]) if restrict else 9
        for digit in range(limit + 1):
            cache[key] = max(cache[key], dfs(i + 1, False if digit < limit else restrict, sum + digit))
        return cache[key]

    return dfs(0, True, 0)


for n in [100, 9995, 3141592653589793, 2999]:
    print(x(n), end=' ')
    print(y(n))
