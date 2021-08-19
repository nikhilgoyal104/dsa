from math import inf
import sys

sys.setrecursionlimit(10000)


# T=sn,S=n
def w(nums, tar):
    dp, n = {}, len(nums)

    def dfs(start, tar):
        if not tar:
            return 0
        if tar < 0:
            return inf
        key = start, tar
        if key in dp:
            return dp[key]
        dp[key] = inf
        for i in range(start, n):
            dp[key] = min(dp[key], 1 + dfs(i, tar - nums[i]))
        return dp[key]

    res = dfs(0, tar)
    return -1 if res == inf else res


# T=sn,S=n
def x(nums, tar):
    dp, n = {0: 0}, len(nums)

    def dfs(tar):
        if tar < 0:
            return inf
        if tar in dp:
            return dp[tar]
        dp[tar] = inf
        for val in nums:
            dp[tar] = min(dp[tar], 1 + dfs(tar - val))
        return dp[tar]

    res = dfs(tar)
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


for nums, tar in [
    ([1, 2, 5], 11),
    ([2], 3),
    ([1], 0),
    ([1], 1),
    ([3, 7, 405, 436], 8839),
    ([474, 83, 404, 3], 264)
]:
    print(w(nums, tar), end=' ')
    print(x(nums, tar), end=' ')
    print(y(nums, tar), end=' ')
    print(z(nums, tar))
