from math import inf

inputs = [
    [10, 15, 20],
    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
]


# T=2ⁿ,S=n
def main(nums):
    n = len(nums)

    def dfs(i):
        if i == n:
            return 0
        if i > n:
            return inf
        res = inf
        for jump in [1, 2]:
            res = min(res, nums[i] + dfs(i + jump))
        return res

    return min(dfs(i) for i in [0, 1])


for nums in inputs:
    print(main(nums))


# T=n,S=n
def main(nums):
    n = len(nums)
    cache = {n: 0}

    def dfs(i):
        if i in cache:
            return cache[i]
        if i > n:
            return inf
        cache[i] = inf
        for jump in [1, 2]:
            cache[i] = min(cache[i], nums[i] + dfs(i + jump))
        return cache[i]

    return min(dfs(i) for i in [0, 1])


for nums in inputs:
    print(main(nums))


# T=n,S=n
def main(nums):
    n = len(nums)

    def dfs(i):
        if i in [0, 1]:
            return 0
        if i < 0:
            return inf
        res = inf
        for jump in [1, 2]:
            res = min(res, nums[i - jump] + dfs(i - jump))
        return res

    return dfs(n)


for nums in inputs:
    print(main(nums))


# T=n,S=n
def main(nums):
    n = len(nums)
    cache = {0: 0, 1: 0}

    def dfs(i):
        if i in cache:
            return cache[i]
        if i < 0:
            return inf
        cache[i] = inf
        for jump in [1, 2]:
            cache[i] = min(cache[i], nums[i - jump] + dfs(i - jump))
        return cache[i]

    return dfs(n)


for nums in inputs:
    print(main(nums))


# T=n,S=n
def main(nums):
    n = len(nums)
    cache = [0] * (n + 1)
    cache[0], cache[1] = 0, 0
    for i in range(2, n + 1):
        cache[i] = min(nums[i - 1] + cache[i - 1], nums[i - 2] + cache[i - 2])
    return cache[-1]


for nums in inputs:
    print(main(nums))
