from math import inf


# T=n²,S=1
def x(nums):
    n, profit = len(nums), 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            profit = max(profit, nums[j] - nums[i])
    return profit


# T=n,S=1
def y(nums):
    least, profit = inf, 0
    for val in nums:
        profit = max(profit, val - least)
        least = min(least, val)
    return profit


def z(nums):
    n, dp = len(nums), {}

    def dfs(i, stock, k):
        if i == n or k == 0:
            return 0
        key = i, stock, k
        if key in dp:
            return dp[key]
        if stock:
            dp[key] = max(dfs(i + 1, False, k - 1) + nums[i], dfs(i + 1, stock, k))
        else:
            dp[key] = max(dfs(i + 1, True, k) - nums[i], dfs(i + 1, stock, k))
        return dp[key]

    return dfs(0, False, 1)


for nums in [
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
