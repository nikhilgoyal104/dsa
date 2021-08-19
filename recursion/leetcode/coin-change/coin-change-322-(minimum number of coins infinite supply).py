from math import inf
import sys

sys.setrecursionlimit(10000)


# T=sn,S=n
def w(nums, total):
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
def x(nums, total):
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


# T=sn,S=n
def y(coins, n):
    dp = [inf] * (n + 1)
    dp[0] = 0
    for target in range(1, n + 1):
        for coin in coins:
            if target >= coin:
                dp[target] = min(dp[target], 1 + dp[target - coin])
    return -1 if dp[-1] == inf else dp[-1]


# T=sn,S=n
def z(coins, n):
    dp = [inf] * (n + 1)
    dp[0] = 0
    for coin in coins:
        for target in range(coin, n + 1):
            dp[target] = min(dp[target], 1 + dp[target - coin])
    return -1 if dp[-1] == inf else dp[-1]


for nums, total in [
    ([1, 2, 5], 11),
    ([2], 3),
    ([1], 0),
    ([1], 1),
    ([3, 7, 405, 436], 8839),
    ([474, 83, 404, 3], 264)
]:
    print(w(nums, total), end=' ')
    print(x(nums, total), end=' ')
    print(y(nums, total), end=' ')
    print(z(nums, total))
