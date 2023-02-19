from math import inf, sqrt


# T=n√n,S=n
def x(n):
    nums = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]
    total, size = n, len(nums)
    cache = [[inf] * (total + 1) for _ in range(size)]
    for j in range(total + 1):
        quot, rem = divmod(j, nums[0])
        cache[0][j] = quot if not rem else inf
    for i in range(size):
        cache[i][0] = 0
    for i in range(1, size):
        for j in range(1, total + 1):
            cache[i][j] = min(cache[i - 1][j], 1 + (cache[i][j - nums[i]] if j >= nums[i] else inf))
    return cache[-1][-1]


for n in [
    12, 13, 40, 143, 6554, 7168
]:
    print(x(n))
