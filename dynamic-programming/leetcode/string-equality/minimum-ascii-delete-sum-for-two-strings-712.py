# T=mn,S=mn
def x(s1, s2):
    cache = {}

    def dfs(s1, s2):
        if not s1:
            return sum(ord(char) for char in s2)
        if not s2:
            return sum(ord(char) for char in s1)
        key = s1, s2
        if key in cache:
            return cache[key]
        if s1[0] != s2[0]:
            cache[key] = min(ord(s1[0]) + dfs(s1[1:], s2), ord(s2[0]) + dfs(s1, s2[1:]))
            return cache[key]
        cache[key] = dfs(s1[1:], s2[1:])
        return cache[key]

    return dfs(s1, s2)


# T=mn,S=mn
# cache[i][j] = f(s1[:i],s2[:j])
def y(s1, s2):
    m, n = len(s1), len(s2)
    cache = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if not i:
                cache[i][j] = cache[0][j - 1] + ord(s2[j - 1]) if j else 0
            elif not j:
                cache[i][j] = cache[i - 1][0] + ord(s1[i - 1]) if i else 0
            elif s1[i - 1] != s2[j - 1]:
                cache[i][j] = min(ord(s1[i - 1]) + cache[i - 1][j], ord(s2[j - 1]) + cache[i][j - 1])
            else:
                cache[i][j] = cache[i - 1][j - 1]
    return cache[-1][-1]


for s1, s2 in [
    ('sea', 'eat'),
    ('delete', 'leet'),
    ('nbzvshnmtlioe', 'rudntqxfmslvpib')
]:
    print(x(s1, s2), end=' ')
    print(y(s1, s2))
