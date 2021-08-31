# T=n³,S=1
def x(nums):
    res = 0
    for val in nums:
        size = 1
        while val + size in nums:
            size += 1
        res = max(res, size)
    return res


# T=nlogn,S=1
def y(nums):
    n, res, nums = len(nums), 0, sorted(nums)
    for i in range(1, n):
        size = 1
        while i < n and nums[i] - nums[i - 1] == 1:
            size += 1
            i += 1
        res = max(res, size)
    return res


# T=n,S=n
def z(nums):
    numsSet, res = set(nums), 0
    for val in nums:
        if val - 1 not in numsSet:
            size = 1
            while val + 1 in numsSet:
                val, size = val + 1, size + 1
            res = max(res, size)
    return res


for nums in [
    [100, 4, 200, 1, 3, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
    [10, 5, 9, 1, 11, 8, 6, 15, 3, 12, 2]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums), end=' ')
    print()
