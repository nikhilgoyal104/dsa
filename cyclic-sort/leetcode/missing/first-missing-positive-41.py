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
    res = 1
    numSet = set(nums)
    while res in numSet:
        res += 1
    return res


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=nlogn,S=n
def main(nums):
    nums = sorted(nums)
    res = 1
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
    presentIndex = 0
    while presentIndex < n:
        correctIndex = nums[presentIndex] - 1
        if -1 < correctIndex < n and nums[presentIndex] != nums[correctIndex]:
            nums[correctIndex], nums[presentIndex] = nums[presentIndex], nums[correctIndex]
        else:
            presentIndex += 1
    for presentIndex in range(n):
        if presentIndex != nums[presentIndex] - 1:
            return presentIndex + 1
    return n + 1


for nums in inputs:
    print(main(nums), nums)
