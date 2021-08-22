def x(s1, s2):
    m, n = len(s1), len(s2)

    def dfs(i, j):
        if i == m or j == n:
            return 0
        if s1[i] == s2[j]:
            return 1 + dfs(i + 1, j + 1)
        return max(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))

    return dfs(0, 0)


for s1, s2 in [
    ('abdca', 'cbda'),
    ('passport', 'ppsspt'),
    ('GeeksforGeeks', 'GeeksQuiz'),
    ('abcdxyz', 'xyzabcd'),
    ('zxabcdezy', 'yzabcdezx')
]:
    print(x(s1, s2))
