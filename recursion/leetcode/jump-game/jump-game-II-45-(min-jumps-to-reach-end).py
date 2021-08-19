from math import inf


# T=n²,S=n
def x(nums):
    target = len(nums) - 1
    dp = {target: 0}

    def dfs(i):
        if i in dp:
            return dp[i]
        dp[i] = inf
        for val in range(min(nums[i], target - i), 0, -1):
            dp[i] = min(dp[i], 1 + dfs(i + val))
        return dp[i]

    return dfs(0)


# T=n²,S=n
def y(nums):
    n = len(nums)
    dp = [inf] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if j + nums[j] >= i:
                dp[i] = min(dp[i], 1 + dp[j])
    return dp[-1]


# T=n²,S=n
def z(nums):
    n = len(nums)
    dp = [inf] * n
    dp[-1] = 0
    for i in range(n - 2, -1, -1):
        for j in range(1, nums[i] + 1):
            if i + j < n:
                dp[i] = min(dp[i], 1 + dp[i + j])
    return dp[0]


for nums in [
    [2, 3, 1, 1, 4],
    [2, 3, 0, 1, 4]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
