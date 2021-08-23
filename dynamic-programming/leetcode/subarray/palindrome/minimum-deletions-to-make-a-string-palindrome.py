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
    n, dp = len(s), {}

    def dfs(i, j):
        if i >= j:
            return 0
        key = i, j
        if key in dp:
            return dp[key]
        if s[i] == s[j]:
            dp[key] = dfs(i + 1, j - 1)
            return dp[key]
        dp[key] = 1 + min(dfs(i + 1, j), dfs(i, j - 1))
        return dp[key]

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
