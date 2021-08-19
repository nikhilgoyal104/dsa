def x(n, k):
    def dfs(i, prev):
        if i == n:
            return 1
        count = 0
        for choice in range(1, k + 1):
            if choice == prev:
                continue
            count += dfs(i + 1, choice)
        return count

    return dfs(0, 0)


def y(n, k):
    dp = {}

    def dfs(i, prev):
        if i == n:
            return 1
        key = i, prev
        if key in dp:
            return dp[key]
        dp[key] = 0
        for choice in range(1, k + 1):
            if choice == prev:
                continue
            dp[key] += dfs(i + 1, choice)
        return dp[key]

    return dfs(0, 0)


for n, k in [
    (3, 2),
    (1, 1),
    (7, 2),
]:
    print(x(n, k), end=' ')
    print(y(n, k))
