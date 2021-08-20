from math import inf
import sys

sys.setrecursionlimit(10000)


# T=sn,S=n
def x(nums, total):
    dp, n = {}, len(nums)

    def dfs(start, total):
        if not total:
            return 0
        if total < 0:
            return inf
        key = start, total
        if key in dp:
            return dp[key]
        dp[key] = inf
        for i in range(start, n):
            dp[key] = min(dp[key], 1 + dfs(i, total - nums[i]))
        return dp[key]

    res = dfs(0, total)
    return -1 if res == inf else res


# T=sn,S=n
def y(nums, total):
    dp, n = {0: 0}, len(nums)

    def dfs(total):
        if total < 0:
            return inf
        if total in dp:
            return dp[total]
        dp[total] = inf
        for val in nums:
            dp[total] = min(dp[total], 1 + dfs(total - val))
        return dp[total]

    res = dfs(total)
    return -1 if res == inf else res


# T=ns,S=ns
def z(nums, total):
    n = len(nums)
    dp = [[inf] * (total + 1) for _ in range(n)]
    for j in range(total + 1):
        dp[0][j] = j // nums[0] if not j % nums[0] else 0
    for i in range(n):
        dp[i][0] = 0
    for i in range(1, n):
        for j in range(1, total + 1):
            dp[i][j] = min(dp[i - 1][j], 1 + (dp[i][j - nums[i]] if j >= nums[i] else 0))
    return dp[-1][-1]


for nums, total in [
    ([1, 2, 5], 11),
    ([2], 3),
    ([1], 0),
    ([1], 1),
    ([3, 7, 405, 436], 8839),
    ([474, 83, 404, 3], 264)
]:
    print(x(nums, total), end=' ')
    print(y(nums, total), end=' ')
    print(z(nums, total))
