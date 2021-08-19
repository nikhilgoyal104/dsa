from math import inf


# T=2ⁿ,S=n
def p(nums):
    n = len(nums)

    def dfs(i):
        if i == n:
            return 0
        if i > n:
            return inf
        res = inf
        for val in [1, 2]:
            res = min(res, nums[i] + dfs(i + val))
        return res

    return min(dfs(i) for i in [0, 1])


# T=n,S=n
def q(nums):
    n = len(nums)
    dp = {n: 0}

    def dfs(i):
        if i in dp:
            return dp[i]
        if i > n:
            return inf
        dp[i] = inf
        for val in [1, 2]:
            dp[i] = min(dp[i], nums[i] + dfs(i + val))
        return dp[i]

    return min(dfs(i) for i in [0, 1])


# T=n,S=n
def r(nums):
    def dfs(i):
        if i in [0, 1]:
            return 0
        if i < 0:
            return inf
        res = inf
        for val in [1, 2]:
            res = min(res, nums[i - val] + dfs(i - val))
        return res

    return dfs(len(nums))


# T=n,S=n
def s(nums):
    dp = {0: 0, 1: 0}

    def dfs(i):
        if i in dp:
            return dp[i]
        if i < 0:
            return inf
        dp[i] = inf
        for val in [1, 2]:
            dp[i] = min(dp[i], nums[i - val] + dfs(i - val))
        return dp[i]

    return dfs(len(nums))


# T=n,S=n
def t(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 0
    for i in range(2, n + 1):
        dp[i] = min(nums[i - 1] + dp[i - 1], nums[i - 2] + dp[i - 2])
    return dp[-1]


for nums in [
    [10, 15, 20],
    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
]:
    print(p(nums), end=' ')
    print(q(nums), end=' ')
    print(r(nums), end=' ')
    print(s(nums), end=' ')
    print(t(nums))
