def x(s, p):
    def dfs(s, p):
        if not p:
            return not s
        firstMatch = s and p[0] in {s[0], '.'}
        if len(p) > 1 and p[1] == '*':
            return firstMatch and dfs(s[1:], p) or dfs(s, p[2:])
        return firstMatch and dfs(s[1:], p[1:])

    return dfs(s, p)


# T=sp,S=sp
def y(s, p):
    dp = {}

    def dfs(s, p):
        if not p:
            return not s
        key = s, p
        if key in dp:
            return dp[key]
        firstMatch = s and p[0] in {s[0], '.'}
        if len(p) > 1 and p[1] == '*':
            dp[key] = firstMatch and dfs(s[1:], p) or dfs(s, p[2:])
            return dp[key]
        dp[key] = firstMatch and dfs(s[1:], p[1:])
        return dp[key]

    return dfs(s, p)


for s, p in [
    ('aa', 'a'),
    ('aa', 'a*'),
    ('ab', '.*'),
    ('aab', 'c*a*b'),
    ('aaa', 'a*a'),
    ('ab', '.*c'),
    ('mississippi', 'mis*is*p*.')
]:
    print(x(s, p), end=' ')
    print(y(s, p))
