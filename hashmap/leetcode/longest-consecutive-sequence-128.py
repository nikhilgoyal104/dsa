inputs = [
    [100, 4, 200, 1, 3, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
    [10, 5, 9, 1, 11, 8, 6, 15, 3, 12, 2]
]


# T=n³,S=1
def main(nums):
    res = 0
    for val in nums:
        size = 1
        while val + size in nums:
            size += 1
        res = max(res, size)
    return res


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=nlogn,S=1
def main(nums):
    nums = sorted(nums)
    n, res = len(nums), 0
    for i in range(1, n):
        size = 1
        while i < n and nums[i] - nums[i - 1] == 1:
            size += 1
            i += 1
        res = max(res, size)
    return res


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=n,S=n
def main(nums):
    numsSet, res = set(nums), 0
    for val in nums:
        if val - 1 not in numsSet:
            size = 1
            while val + size in numsSet:
                size += 1
            res = max(res, size)
    return res


for nums in inputs:
    print(main(nums), end=' ')
