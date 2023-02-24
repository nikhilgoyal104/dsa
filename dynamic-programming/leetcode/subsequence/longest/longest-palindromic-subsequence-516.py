# T=2ⁿ,S=n
# LPS(s) = LCS(s,reverse(s))
def u(s):
    n = len(s)
    s1, s2 = s, s[::-1]

    def dfs(i, j):
        if i == n or j == n:
            return 0
        if s1[i] == s2[j]:
            return 1 + dfs(i + 1, j + 1)
        return max(dfs(i + 1, j), dfs(i, j + 1))

    return dfs(0, 0)


# T=2ⁿ,S=n
# LPS(s) = LCS(s,reverse(s))
def v(s):
    n = len(s)

    def dfs(i, j):
        if i == n or j == -1:
            return 0
        if s[i] == s[j]:
            return 1 + dfs(i + 1, j - 1)
        return max(dfs(i + 1, j), dfs(i, j - 1))

    return dfs(0, n - 1)


# T=2ⁿ,S=n
def w(s):
    n = len(s)

    def dfs(i, j):
        if i == j:
            return 1
        if i > j:
            return 0
        if s[i] == s[j]:
            return 2 + dfs(i + 1, j - 1)
        return max(dfs(i + 1, j), dfs(i, j - 1))

    return dfs(0, n - 1)


# T=n²,S=n²
def x(s):
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
        if s[i] == s[j]:
            cache[key] = 2 + dfs(i + 1, j - 1)
            return cache[key]
        cache[key] = max(dfs(i + 1, j), dfs(i, j - 1))
        return cache[key]

    return dfs(0, n - 1)


# T=n²,S=n²
# cache[i][j] = LPS of s[i:j+1]
def y(s):
    n = len(s)
    cache = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                cache[i][j] = 1
            elif s[i] == s[j]:
                cache[i][j] = 2 + cache[i + 1][j - 1]
            else:
                cache[i][j] = max(cache[i][j - 1], cache[i + 1][j])
    return cache[0][-1]


# T=n²,S=n²
# LPS(s) = LCS(s,reverse(s))
def z(s):
    n, s1, s2 = len(s), s, s[::-1]
    cache = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cache[i][j] = 1 + cache[i - 1][j - 1]
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    return cache[-1][-1]


for s in [
    'mnop', 'geeksforgeeks', 'bbbab', 'cbbd', 'abkccbc'
]:
    print(u(s), end=' ')
    print(v(s), end=' ')
    print(w(s), end=' ')
    print(x(s), end=' ')
    print(y(s), end=' ')
    print(z(s))
