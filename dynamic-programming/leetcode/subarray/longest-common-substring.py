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
    m, n, dp = len(s1), len(s2), {}

    def dfs(i, j, count):
        if i == m or j == n:
            return count
        key = i, j, count
        if key in dp:
            return dp[key]
        if s1[i] == s2[j]:
            count = dfs(i + 1, j + 1, count + 1)
        dp[key] = max(count, dfs(i + 1, j, 0), dfs(i, j + 1, 0))
        return dp[key]

    return dfs(0, 0, 0)


for s1, s2 in [
    ('abdca', 'cbda'),
    ('passport', 'ppsspt'),
    ('GeeksforGeeks', 'GeeksQuiz'),
    ('abcdxyz', 'xyzabcd'),
    ('zxabcdezy', 'yzabcdezx')
]:
    print(x(s1, s2), end=' ')
    print(y(s1, s2))
