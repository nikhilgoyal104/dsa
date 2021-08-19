from math import inf
from heapq import *
from collections import deque


# T=kⁿ,S=n
def x(nums, k):
    n = len(nums)

    def dfs(i):
        if i == n - 1:
            return nums[i]
        if i > n - 1:
            return -inf
        maximum = -inf
        for val in range(1, k + 1):
            maximum = max(maximum, nums[i] + dfs(i + val))
        return maximum

    return dfs(0)


# T=kn,S=n
def y(nums, k):
    n = len(nums)
    dp = {n - 1: nums[n - 1]}

    def dfs(i):
        if i > n - 1:
            return -inf
        if i in dp:
            return dp[i]
        dp[i] = -inf
        for val in range(1, k + 1):
            dp[i] = max(dp[i], nums[i] + dfs(i + val))
        return dp[i]

    return dfs(0)


# T=kn,S=n
def p(nums, k):
    n = len(nums)
    dp = [-inf] * n
    dp[0] = nums[0]
    for i in range(1, n):
        for j in range(1, k + 1):
            if i - j > -1:
                dp[i] = max(dp[i], dp[i - j] + nums[i])
    return dp[-1]


# T=kn,S=n
def q(nums, k):
    n = len(nums)
    dp = [-inf] * n
    dp[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        for j in range(1, k + 1):
            if i + j < n:
                dp[i] = max(dp[i], dp[i + j] + nums[i])
    return dp[0]


# T=n,S=n
def r(nums, k):
    n = len(nums)
    dp, dq = [0] * n, deque([0])
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = dp[dq[0]] + nums[i]
        while dq and dp[i] > dp[dq[-1]]:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
    return dp[-1]


# T=n,S=k
def s(nums, k):
    n = len(nums)
    dq, res = deque([(0, nums[0])]), nums[0]
    for i in range(1, n):
        res = dq[0][1] + nums[i]
        while dq and res > dq[-1][1]:
            dq.pop()
        dq.append((i, nums[i]))
        if dq[0][0] == i - k:
            dq.popleft()
    return res


for nums, k in [
    ([1, -1, -2, 4, -7, 3], 2),
    ([10, -5, -2, 4, 0, 3], 3),
    ([1, -5, -20, 4, -1, 3, -6, -3], 2)
]:
    print(x(nums, k), end=' ')
    print(y(nums, k), end=' ')
    print(p(nums, k), end=' ')
    print(q(nums, k), end=' ')
    print(r(nums, k), end=' ')
    print(s(nums, k))
