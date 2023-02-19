# T=2ⁿ,S=n
def x(s1, s2):
    m, n = len(s1), len(s2)

    def dfs(i, j, count):
        if i == m or j == n:
            return count
        if s1[i] == s2[j]:
            count = dfs(i + 1, j + 1, count + 1)
        return max(count, dfs(i + 1, j, 0), dfs(i, j + 1, 0))

    return dfs(0, 0, 0)


# T=mn,S=mn
def y(s1, s2):
    m, n = len(s1), len(s2)
    cache = {}

    def dfs(i, j, count):
        if i == m or j == n:
            return count
        key = i, j, count
        if key in cache:
            return cache[key]
        if s1[i] == s2[j]:
            count = dfs(i + 1, j + 1, count + 1)
        cache[key] = max(count, dfs(i + 1, j, 0), dfs(i, j + 1, 0))
        return cache[key]

    return dfs(0, 0, 0)


# T=mn,S=mn
# cache[i][j] = longest common suffix of s1[:i] and s2[:j]
def z(s1, s2):
    m, n = len(s1), len(s2)
    res = 0
    cache = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cache[i][j] = 1 + cache[i - 1][j - 1]
                res = max(res, cache[i][j])
    return res


for s1, s2 in [
    ('abdca', 'cbda'),
    ('passport', 'ppsspt'),
    ('GeeksforGeeks', 'GeeksQuiz'),
    ('abcdxyz', 'xyzabcd'),
    ('zxabcdezy', 'yzabcdezx'),
    ('pqabcxy', 'xyzabcp')
]:
    print(x(s1, s2), end=' ')
    print(y(s1, s2), end=' ')
    print(z(s1, s2))
