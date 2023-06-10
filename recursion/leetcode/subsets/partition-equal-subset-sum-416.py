# T=ns,S=ns
def x(nums):
    if sum(nums) % 2:
        return False
    n = len(nums)
    total = sum(nums) // 2
    cache = {}

    def dfs(start, sum):
        if sum == total:
            return True
        if sum > total:
            return False
        key = start, sum
        if key in cache:
            return cache[key]
        for i in range(start, n):
            if dfs(i + 1, sum + nums[i]):
                cache[key] = True
                return cache[key]
        cache[key] = False
        return cache[key]

    return dfs(0, 0)


# T=ns,S=ns
def y(nums):
    if sum(nums) % 2:
        return False
    n = len(nums)
    total = sum(nums) // 2
    cache = {}

    def dfs(i, sum):
        if sum == total:
            return True
        if sum > total or i == n:
            return False
        key = i, sum
        if key in cache:
            return cache[key]
        cache[key] = dfs(i + 1, sum + nums[i]) or dfs(i + 1, sum)
        return cache[key]

    return dfs(0, 0)


# T=ns,S=ns
# cache[i][j] = is sum of numbers till index i equal to j
def z(nums):
    if sum(nums) % 2:
        return False
    n = len(nums)
    total = sum(nums) // 2
    cache = [[False] * (total + 1) for _ in range(n)]
    for j in range(total + 1):
        cache[0][j] = nums[0] == j
    for i in range(n):
        cache[i][0] = True
    for i in range(1, n):
        for j in range(1, total + 1):
            cache[i][j] = cache[i - 1][j] or (j >= nums[i] and cache[i - 1][j - nums[i]])
    return cache[-1][-1]


for nums in [
    [1, 2, 5],
    [1, 5, 11, 5],
    [1, 2, 3, 5],
    [2, 2, 3, 5],
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 97]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
