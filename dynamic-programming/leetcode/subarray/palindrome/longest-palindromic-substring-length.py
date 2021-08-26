# T=2ⁿ,S=n
def x(s):
    n = len(s)

    def dfs(i, j):
        if i == j:
            return 1
        if i > j:
            return 0
        if s[i] == s[j] and j - i - 1 == dfs(i + 1, j - 1):
            return 2 + (j - i - 1)
        return max(dfs(i + 1, j), dfs(i, j - 1))

    return dfs(0, n - 1)


# T=n²,S=n²
def y(s):
    n, dp = len(s), {}

    def dfs(i, j):
        if i == j:
            return 1
        if i > j:
            return 0
        key = i, j
        if key in dp:
            return dp[key]
        if s[i] == s[j] and j - i - 1 == dfs(i + 1, j - 1):
            dp[key] = 2 + (j - i - 1)
            return dp[key]
        dp[key] = max(dfs(i + 1, j), dfs(i, j - 1))
        return dp[key]

    return dfs(0, n - 1)


for s in [
    'abdbca',
    'cddpd',
    'pqr',
    'aaaabbaa',
    'banana'
]:
    print(x(s), end=' ')
    print(y(s))
