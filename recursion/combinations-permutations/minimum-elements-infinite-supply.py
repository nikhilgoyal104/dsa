from math import inf
from collections import deque


def w(nums, total):
    n, dp = len(nums), {}

    def dfs(start, sum):
        if sum == total:
            return 0
        if sum > total:
            return inf
        key = start, sum
        if key in dp:
            return dp[key]
        dp[key] = inf
        for i in range(start, n):
            dp[key] = min(dp[key], 1 + dfs(i, sum + nums[i]))
        return dp[key]

    return dfs(0, 0)


def x(nums, total):
    dp = {total: 0}

    def dfs(sum):
        if sum > total:
            return inf
        if sum in dp:
            return dp[sum]
        dp[sum] = inf
        for val in nums:
            dp[sum] = min(dp[sum], 1 + dfs(sum + val))
        return dp[sum]

    return dfs(0)


def y(nums, total):
    queue = deque([(0, 0)])
    while queue:
        sum, count = queue.popleft()
        if sum == total:
            return count
        if sum > total:
            continue
        for val in nums:
            queue.append((sum + val, count + 1))


for nums, total in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 11),
    ([1, 2, 5], 11),
]:
    print(w(nums, total), end=' ')
    print(x(nums, total), end=' ')
    print(y(nums, total))

print()


# T=ns,S=ns
def z(nums, total):
    n = len(nums)
    dp = [[inf] * (total + 1) for _ in range(n)]
    for j in range(total + 1):
        quot, rem = divmod(j, nums[0])
        dp[0][j] = quot if not rem else inf
    for i in range(n):
        dp[i][0] = 0
    for i in range(1, n):
        for j in range(1, total + 1):
            dp[i][j] = min(dp[i - 1][j], 1 + (dp[i][j - nums[i]] if j >= nums[i] else inf))
    return dp[-1][-1]


for nums, total in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 11),
    ([1, 2, 5], 11),
    ([2], 3),
    ([1], 0),
    ([1], 1),
    ([3, 7, 405, 436], 8839),
    ([474, 83, 404, 3], 264)
]:
    print(z(nums, total))
