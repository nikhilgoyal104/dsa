# f(s) = len(s) - LPS(s)
# LPS(s) = LCS(s,reverse(s))
# T=n²,S=n²
def x(s):
    n, cache = len(s), {}

    def dfs(i, j):
        if i == n or j == -1:
            return 0
        key = i, j
        if key in cache:
            return cache[key]
        if s[i] == s[j]:
            cache[key] = 1 + dfs(i + 1, j - 1)
            return cache[key]
        cache[key] = max(dfs(i + 1, j), dfs(i, j - 1))
        return cache[key]

    return n - dfs(0, n - 1)


for s in [
    'zzazz',
    'mbadm',
    'leetcode'
]:
    print(x(s))
