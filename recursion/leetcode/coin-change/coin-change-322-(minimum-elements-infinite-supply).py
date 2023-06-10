import sys

sys.setrecursionlimit(10000)


# T=sn,S=n
def x(nums, total):
    n = len(nums)
    cache = {}

    def dfs(start, sum):
        if sum == total:
            return 0
        if sum > total:
            return float('inf')
        key = start, sum
        if key in cache:
            return cache[key]
        cache[key] = float('inf')
        for i in range(start, n):
            cache[key] = min(cache[key], 1 + dfs(i, sum + nums[i]))
        return cache[key]

    res = dfs(0, 0)
    return -1 if res == float('inf') else res


# T=sn,S=n
def y(nums, total):
    cache = {total: 0}

    def dfs(sum):
        if sum > total:
            return float('inf')
        if sum in cache:
            return cache[sum]
        cache[sum] = float('inf')
        for val in nums:
            cache[sum] = min(cache[sum], 1 + dfs(sum + val))
        return cache[sum]

    res = dfs(0)
    return -1 if res == float('inf') else res


# T=ns,S=ns
def z(nums, total):
    n = len(nums)
    cache = [[float('inf')] * (total + 1) for _ in range(n)]
    for j in range(total + 1):
        quot, rem = divmod(j, nums[0])
        cache[0][j] = quot if not rem else float('inf')
    for i in range(n):
        cache[i][0] = 0
    for i in range(1, n):
        for j in range(1, total + 1):
            cache[i][j] = min(cache[i - 1][j], 1 + (cache[i][j - nums[i]] if j >= nums[i] else float('inf')))
    return -1 if cache[-1][-1] == float('inf') else cache[-1][-1]


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
