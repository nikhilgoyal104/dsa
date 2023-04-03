from heapq import *
from collections import deque


# T=kⁿ,S=n
def x(nums, k):
    n = len(nums)

    def dfs(i):
        if i == n - 1:
            return nums[i]
        if i > n - 1:
            return float('-inf')
        res = float('-inf')
        for val in range(1, k + 1):
            res = max(res, nums[i] + dfs(i + val))
        return res

    return dfs(0)


# T=kn,S=n
def y(nums, k):
    n = len(nums)
    cache = {n - 1: nums[n - 1]}

    def dfs(i):
        if i > n - 1:
            return float('-inf')
        if i in cache:
            return cache[i]
        cache[i] = float('-inf')
        for val in range(1, k + 1):
            cache[i] = max(cache[i], nums[i] + dfs(i + val))
        return cache[i]

    return dfs(0)


# T=kn,S=n
def p(nums, k):
    n = len(nums)
    cache = [float('-inf')] * n
    cache[0] = nums[0]
    for i in range(1, n):
        for j in range(1, k + 1):
            if i - j > -1:
                cache[i] = max(cache[i], cache[i - j] + nums[i])
    return cache[-1]


# T=kn,S=n
def q(nums, k):
    n = len(nums)
    cache = [float('-inf')] * n
    cache[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        for j in range(1, k + 1):
            if i + j < n:
                cache[i] = max(cache[i], cache[i + j] + nums[i])
    return cache[0]


# T=n,S=n
def r(nums, k):
    n = len(nums)
    cache = [0] * n
    queue = deque([0])
    cache[0] = nums[0]
    for i in range(1, n):
        cache[i] = cache[queue[0]] + nums[i]
        while queue and cache[i] > cache[queue[-1]]:
            queue.pop()
        queue.append(i)
        if queue[0] == i - k:
            queue.popleft()
    return cache[-1]


# T=n,S=k
def s(nums, k):
    n = len(nums)
    queue = deque([(0, nums[0])])
    res = nums[0]
    for i in range(1, n):
        res = queue[0][1] + nums[i]
        while queue and res > queue[-1][1]:
            queue.pop()
        queue.append((i, nums[i]))
        if queue[0][0] == i - k:
            queue.popleft()
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
