# T=n²,S=1
def x(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# T=n,S=n
def y(nums, target):
    n = len(nums)
    valToIndex = {nums[i]: i for i in range(n)}
    for i in range(n):
        complement = target - nums[i]
        if complement in valToIndex and valToIndex[complement] != i:
            return [i, valToIndex[complement]]
    return []


# T=n,S=n
def z(nums, target):
    n = len(nums)
    valToIndex = {}
    for i in range(n):
        complement = target - nums[i]
        if complement in valToIndex:
            return [valToIndex[complement], i]
        valToIndex[nums[i]] = i
    return []


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
