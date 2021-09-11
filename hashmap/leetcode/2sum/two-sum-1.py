# T=n²,S=1
def x(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


# T=n,S=n
def y(nums, target):
    n = len(nums)
    valToIndex = {nums[i]: i for i in range(n)}
    for i in range(n):
        key = target - nums[i]
        if key in valToIndex and valToIndex[key] != i:
            return [i, valToIndex[key]]


# T=n,S=n
def z(nums, target):
    valToIndex = {}
    for i, val in enumerate(nums):
        if target - val in valToIndex:
            return [valToIndex[target - val], i]
        valToIndex[val] = i


for nums, target in [
    ([3, 4, 9, 6, 4], 8),
    ([4, -2, 4, 0, 6, 3, 2, 7], 1),
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6)
]:
    print(x(nums, target), end=' ')
    print(y(nums, target), end=' ')
    print(z(nums, target))
