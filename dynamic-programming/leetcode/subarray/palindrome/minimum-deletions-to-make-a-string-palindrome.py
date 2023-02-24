# T=2ⁿ,S=n
def x(s):
    n = len(s)

    def dfs(i, j):
        if i >= j:
            return 0
        if s[i] == s[j]:
            return dfs(i + 1, j - 1)
        return 1 + min(dfs(i + 1, j), dfs(i, j - 1))

    return dfs(0, n - 1)


# T=n²,S=n²
def y(s):
    n = len(s)
    cache = {}

    def dfs(i, j):
        if i >= j:
            return 0
        key = i, j
        if key in cache:
            return cache[key]
        if s[i] == s[j]:
            cache[key] = dfs(i + 1, j - 1)
            return cache[key]
        cache[key] = 1 + min(dfs(i + 1, j), dfs(i, j - 1))
        return cache[key]

    return dfs(0, n - 1)


# f(s) = len(s) - LPS(s)
# LPS(s) = LCS(s,reverse(s))
def z(s):
    pass


for s in [
    'geeksforgeeks',
    'aebcbda',
    'abdbca',
    'cddpd',
    'pqr'
]:
    print(x(s), end=' ')
    print(y(s))
