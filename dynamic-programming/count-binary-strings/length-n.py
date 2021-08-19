def w(n):
    def dfs(i):
        if i == n:
            return 1
        return dfs(i + 1) + dfs(i + 1)

    return dfs(0)


def x(n):
    dp = {n: 1}

    def dfs(i):
        if i in dp:
            return dp[i]
        dp[i] = dfs(i + 1) + dfs(i + 1)
        return dp[i]

    return dfs(0)


def y(n):
    def dfs(i):
        if i == n:
            return 1
        count = 0
        for _ in [0, 1]:
            count += dfs(i + 1)
        return count

    return dfs(0)


def z(n):
    dp = {n: 1}

    def dfs(i):
        if i in dp:
            return dp[i]
        dp[i] = 0
        for _ in [0, 1]:
            dp[i] += dfs(i + 1)
        return dp[i]

    return dfs(0)


for n in [1, 2, 3, 4]:
    print(w(n), end=' ')
    print(x(n), end=' ')
    print(y(n), end=' ')
    print(z(n))
