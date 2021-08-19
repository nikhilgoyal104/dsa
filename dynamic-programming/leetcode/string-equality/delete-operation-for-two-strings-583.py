# T=mn,S=mn
def x(s1, s2):
    dp = {}

    def dfs(s1, s2):
        if not s2:
            return len(s1)
        if not s1:
            return len(s2)
        key = s1, s2
        if key in dp:
            return dp[key]
        if s1[0] != s2[0]:
            dp[key] = 1 + min(dfs(s1[1:], s2), dfs(s1, s2[1:]))
            return dp[key]
        dp[key] = dfs(s1[1:], s2[1:])
        return dp[key]

    return dfs(s1, s2)


# T=mn,S=mn
def y(s1, s2):
    m, n, dp = len(s1), len(s2), {}

    def dfs(i, j):
        if i == m:
            return n - j
        if j == n:
            return m - i
        key = i, j
        if key in dp:
            return dp[key]
        if s1[i] != s2[j]:
            dp[key] = 1 + min(dfs(i + 1, j), dfs(i, j + 1))
            return dp[key]
        dp[key] = dfs(i + 1, j + 1)
        return dp[key]

    return dfs(0, 0)


# T=mn,S=mn
# dp[i][j] = f(s1[:i],s2[:j])
def z(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if not i or not j:
                dp[i][j] = i + j
            elif s1[i - 1] != s2[j - 1]:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[-1][-1]


for s1, s2 in [
    ('sea', 'eat'),
    ('leetcode', 'etco'),
    ('dinitrophenylhydrazine', 'acetylphenylhydrazine')
]:
    print(x(s1, s2), end=' ')
    print(y(s1, s2), end=' ')
    print(z(s1, s2))
