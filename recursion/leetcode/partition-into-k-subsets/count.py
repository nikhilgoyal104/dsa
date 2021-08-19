# T=nk,S=nk
def x(n, k):
    dp = {}

    def dfs(n, k):
        if not n or not k or k > n:
            return 0
        if n == k or k == 1:
            return 1
        key = n, k
        if key in dp:
            return dp[key]
        dp[key] = dfs(n - 1, k - 1) + k * dfs(n - 1, k)
        return dp[key]

    return dfs(n, k)


for n, k in [
    (4, 3), (3, 2), (3, 1)
]:
    print(x(n, k))
