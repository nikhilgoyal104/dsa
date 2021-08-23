# f(s) = len(s) - LPS(s)
# LPS(s) = LCS(s,reverse(s))
# T=n²,S=n²
def x(s):
    n, dp = len(s), {}

    def dfs(i, j):
        if i == n or j == -1:
            return 0
        key = i, j
        if key in dp:
            return dp[key]
        if s[i] == s[j]:
            dp[key] = 1 + dfs(i + 1, j - 1)
            return dp[key]
        dp[key] = max(dfs(i + 1, j), dfs(i, j - 1))
        return dp[key]

    return n - dfs(0, n - 1)


for s in [
    'zzazz',
    'mbadm',
    'leetcode'
]:
    print(x(s))
