# T=2ⁿ,S=n
def x(s1, s2):
    m, n = len(s1), len(s2)

    def dfs(i, j):
        if i == m or j == n:
            return 0
        if s1[i] == s2[j]:
            return 1 + dfs(i + 1, j + 1)
        return max(dfs(i + 1, j), dfs(i, j + 1))

    return dfs(0, 0)


# T=mn,S=mn
def y(s1, s2):
    m, n, dp = len(s1), len(s2), {}

    def dfs(i, j):
        if i == m or j == n:
            return 0
        key = i, j
        if key in dp:
            return dp[key]
        if s1[i] == s2[j]:
            dp[key] = 1 + dfs(i + 1, j + 1)
            return dp[key]
        dp[key] = max(dfs(i + 1, j), dfs(i, j + 1))
        return dp[key]

    return dfs(0, 0)


# T=mn,S=mn
# dp[i][j] = LCS of s1[:i] and s2[:j]
def z(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


for s1, s2 in [
    ('abcdgh', 'aedfhr'),
    ('gxtxayb', 'aggtab'),
    ('abcde', 'ace'),
    ('abcde', 'ace'),
    ('abc', 'abc'),
    ('abc', 'def')
]:
    print(x(s1, s2), end=' ')
    print(y(s1, s2), end=' ')
    print(z(s1, s2))
