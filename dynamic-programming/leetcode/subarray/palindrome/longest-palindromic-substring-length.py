# T=2ⁿ,S=n
def x(s):
    n = len(s)

    def dfs(i, j):
        if i == j:
            return 1
        if i > j:
            return 0
        if s[i] == s[j] and j - i - 1 == dfs(i + 1, j - 1):
            return 2 + (j - i - 1)
        return max(dfs(i + 1, j), dfs(i, j - 1))

    return dfs(0, n - 1)


# T=n²,S=n²
def y(s):
    n = len(s)
    cache = {}

    def dfs(i, j):
        if i == j:
            return 1
        if i > j:
            return 0
        key = i, j
        if key in cache:
            return cache[key]
        if s[i] == s[j] and j - i - 1 == dfs(i + 1, j - 1):
            cache[key] = 2 + (j - i - 1)
            return cache[key]
        cache[key] = max(dfs(i + 1, j), dfs(i, j - 1))
        return cache[key]

    return dfs(0, n - 1)


for s in [
    'abdbca',
    'cddpd',
    'pqr',
    'aaaabbaa',
    'banana'
]:
    print(x(s), end=' ')
    print(y(s))
