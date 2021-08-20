from math import inf
from collections import deque


def v(nums, total):
    def dfs(start, total, dp):
        if not total:
            return 0
        if total < 0:
            return 0
        key = start, total
        if key in dp:
            return dp[key]
        dp[key] = inf
        for i in range(start, len(nums)):
            dp[key] = min(dp[key], 1 + dfs(i, total - nums[i], dp))
        return dp[key]

    return dfs(0, total, {})


def w(nums, total):
    def dfs(total, dp):
        if total < 0:
            return 0
        if total in dp:
            return dp[total]
        dp[total] = inf
        for val in nums:
            dp[total] = min(dp[total], 1 + dfs(total - val, dp))
        return dp[total]

    return dfs(total, {0: 0})


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


def z(nums, total):
    queue = deque([(total, 0)])
    while queue:
        total, count = queue.popleft()
        if not total:
            return count
        for val in nums:
            queue.append((total - val, count + 1))


for nums, total in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 11)
]:
    print(v(nums, total), end=' ')
    print(w(nums, total), end=' ')
    print(x(nums, total), end=' ')
    print(y(nums, total), end=' ')
    print(z(nums, total))
