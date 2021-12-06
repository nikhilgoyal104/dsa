inputs = [
    [1],
    [0, 2, 2, 1, 1],
    [4, 5, 6],
    [1, 2, 3],
    [1, 2, 0],
    [3, 4, -1, 1],
    [7, 8, 9, 11, 12],
    [-2, 11, 1, -3, 2, 10, 4]
]


# T=n²,S=1
def main(nums):
    res = 1
    while res in nums:
        res += 1
    return res


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=n,S=n
def main(nums):
    numsSet, res = set(nums), 1
    while res in numsSet:
        res += 1
    return res


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=nlogn,S=1
def main(nums):
    nums, res = sorted(nums), 1
    for i in range(len(nums)):
        if nums[i] > res:
            return res
        elif nums[i] == res:
            res += 1
    return res


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=n,S=1
def main(nums):
    n = len(nums)
    for i in range(n):
        dest = nums[i] - 1
        while 1 <= nums[i] <= n and nums[i] != nums[dest]:
            nums[i], nums[dest] = nums[dest], nums[i]
            dest = nums[i] - 1
    for i in range(n):
        if i != nums[i] - 1:
            return i + 1
    return n + 1


for nums in inputs:
    print(main(nums), end=' ')
