# T=mn,S=mn
def x(s1, s2):
    cache = {}

    def dfs(s1, s2):
        if not s1:
            return len(s2)
        if not s2:
            return len(s1)
        key = s1, s2
        if key in cache:
            return cache[key]
        if s1[0] != s2[0]:
            cache[key] = 1 + min(dfs(s1[1:], s2), dfs(s1[1:], s2[1:]), dfs(s1, s2[1:]))
            return cache[key]
        cache[key] = dfs(s1[1:], s2[1:])
        return cache[key]

    return dfs(s1, s2)


# T=mn,S=mn
def y(s1, s2):
    m, n = len(s1), len(s2)
    cache = {}

    def dfs(i, j):
        if i == m:
            return n - j
        if j == n:
            return m - i
        key = i, j
        if key in cache:
            return cache[key]
        if s1[i] != s2[j]:
            cache[key] = 1 + min(dfs(i + 1, j), dfs(i + 1, j + 1), dfs(i, j + 1))
            return cache[key]
        cache[key] = dfs(i + 1, j + 1)
        return cache[key]

    return dfs(0, 0)


# T=mn,S=mn
# cache[i][j] = edit distance of s1[:i] and s2[:j]
def z(s1, s2):
    m, n = len(s1), len(s2)
    cache = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if not i or not j:
                cache[i][j] = i + j
            elif s1[i - 1] == s2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1]
            else:
                cache[i][j] = 1 + min(cache[i - 1][j], cache[i - 1][j - 1], cache[i][j - 1])
    return cache[-1][-1]


for s1, s2 in [
    ('horse', 'ros'),
    ('intention', 'execution'),
    ('park', 'spake'),
    ('dinitrophenylhydrazine', 'acetylphenylhydrazine'),
    ('plasma', 'altruism'),
    ('ahellobye', 'amezooe')
]:
    print(x(s1, s2), end=' ')
    print(y(s1, s2), end=' ')
    print(z(s1, s2))
