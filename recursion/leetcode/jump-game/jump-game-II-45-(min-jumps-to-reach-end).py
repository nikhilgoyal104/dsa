from math import inf


# T=n²,S=n
def x(nums):
    target = len(nums) - 1
    cache = {target: 0}

    def dfs(i):
        if i in cache:
            return cache[i]
        cache[i] = inf
        for val in range(min(nums[i], target - i), 0, -1):
            cache[i] = min(cache[i], 1 + dfs(i + val))
        return cache[i]

    return dfs(0)


# T=n²,S=n
def y(nums):
    n = len(nums)
    cache = [inf] * n
    cache[0] = 0
    for i in range(1, n):
        for j in range(i):
            if j + nums[j] >= i:
                cache[i] = min(cache[i], 1 + cache[j])
    return cache[-1]


# T=n²,S=n
def z(nums):
    n = len(nums)
    cache = [inf] * n
    cache[-1] = 0
    for i in range(n - 2, -1, -1):
        for j in range(1, nums[i] + 1):
            if i + j < n:
                cache[i] = min(cache[i], 1 + cache[i + j])
    return cache[0]


for nums in [
    [2, 3, 1, 1, 4],
    [2, 3, 0, 1, 4]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
