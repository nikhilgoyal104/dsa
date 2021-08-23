# T=2ⁿ,S=n
# LPS(s) = LCS(s,reverse(s))
def u(s):
    n, s1, s2 = len(s), s, s[::-1]

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
    n, dp = len(s), {}

    def dfs(i, j):
        if i == j:
            return 1
        if i > j:
            return 0
        key = i, j
        if key in dp:
            return dp[key]
        if s[i] == s[j]:
            dp[key] = 2 + dfs(i + 1, j - 1)
            return dp[key]
        dp[key] = max(dfs(i + 1, j), dfs(i, j - 1))
        return dp[key]

    return dfs(0, n - 1)


# T=n²,S=n²
# dp[i][j] = LPS of s[i:j+1]
def y(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
            elif s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    return dp[0][-1]


# T=n²,S=n²
# LPS(s) = LCS(s,reverse(s))
def z(s):
    n, s1, s2 = len(s), s, s[::-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


for s in [
    'mnop', 'geeksforgeeks', 'bbbab', 'cbbd', 'abkccbc'
]:
    print(u(s), end=' ')
    print(v(s), end=' ')
    print(w(s), end=' ')
    print(x(s), end=' ')
    print(y(s), end=' ')
    print(z(s))
