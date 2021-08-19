from math import inf
from collections import deque


def v(nums, tar):
    def dfs(start, tar, dp):
        if not tar:
            return 0
        if tar < 0:
            return 0
        key = start, tar
        if key in dp:
            return dp[key]
        dp[key] = inf
        for i in range(start, len(nums)):
            dp[key] = min(dp[key], 1 + dfs(i, tar - nums[i], dp))
        return dp[key]

    return dfs(0, tar, {})


def w(nums, tar):
    def dfs(tar, dp):
        if tar < 0:
            return 0
        if tar in dp:
            return dp[tar]
        dp[tar] = inf
        for val in nums:
            dp[tar] = min(dp[tar], 1 + dfs(tar - val, dp))
        return dp[tar]

    return dfs(tar, {0: 0})


def x(coins, n):
    dp = [inf] * (n + 1)
    dp[0] = 0
    for target in range(1, n + 1):
        for coin in coins:
            if target >= coin:
                dp[target] = min(dp[target], 1 + dp[target - coin])
    return dp[-1]


def y(coins, n):
    dp = [inf] * (n + 1)
    dp[0] = 0
    for coin in coins:
        for target in range(coin, n + 1):
            dp[target] = min(dp[target], 1 + dp[target - coin])
    return dp[-1]


def z(nums, tar):
    queue = deque([(tar, 0)])
    while queue:
        total, count = queue.popleft()
        if not total:
            return count
        for val in nums:
            queue.append((total - val, count + 1))


for nums, tar in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 11)
]:
    print(v(nums, tar), end=' ')
    print(w(nums, tar), end=' ')
    print(x(nums, tar), end=' ')
    print(y(nums, tar), end=' ')
    print(z(nums, tar))
