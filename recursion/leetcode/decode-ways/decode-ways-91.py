# T=n,S=n
def x(s):
    dp = {'': 1}

    def dfs(s):
        if s in dp:
            return dp[s]
        if s[0] == '0':
            return 0
        dp[s] = dfs(s[1:])
        if len(s) >= 2 and int(s[:2]) <= 26:
            dp[s] += dfs(s[2:])
        return dp[s]

    return dfs(s)


# T=n,S=n
def y(s):
    n = len(s)
    dp = {n: 1}

    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == '0':
            return 0
        dp[i] = dfs(i + 1)
        if i < n - 1 and int(s[i:i + 2]) <= 26:
            dp[i] += dfs(i + 2)
        return dp[i]

    return dfs(0)


for s in [
    '12', '123', '226', '0', '06', '27', '1201234', '111111111111111111111111111111111111111111111'
]:
    print(x(s), end=' ')
    print(y(s))
