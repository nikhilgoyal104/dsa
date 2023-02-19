def x(n, k):
    def dfs(i, prev1, prev2):
        if i == n:
            return 1
        count = 0
        for choice in range(1, k + 1):
            if choice == prev1 == prev2:
                continue
            count += dfs(i + 1, choice, prev1)
        return count

    return dfs(0, 0, 0)


def y(n, k):
    cache = {}

    def dfs(i, prev1, prev2):
        if i == n:
            return 1
        key = i, prev1, prev2
        if key in cache:
            return cache[key]
        cache[key] = 0
        for choice in range(1, k + 1):
            if choice == prev1 == prev2:
                continue
            cache[key] += dfs(i + 1, choice, prev1)
        return cache[key]

    return dfs(0, 0, 0)


for n, k in [
    (3, 2),
    (1, 1),
    (7, 2),
]:
    print(x(n, k), end=' ')
    print(y(n, k))
