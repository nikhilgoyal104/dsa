from collections import Counter


# T=n²,S=1
def x(nums):
    res = 0
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            count = Counter(nums[i:j + 1])
            if count[0] == count[1]:
                res = max(res, 2 * count[0])
    return res


# T=n,S=n
def y(nums):
    res = sum = 0
    sumToIndex = {0: -1}
    nums = [-1 if not val else 1 for val in nums]
    for i in range(len(nums)):
        sum += nums[i]
        if sum in sumToIndex:
            res = max(res, i - sumToIndex[sum])
        if sum not in sumToIndex:
            sumToIndex[sum] = i
    return res


# T=n,S=n
def z(nums):
    res = sum = 0
    sumToIndex = {0: -1}
    for i in range(len(nums)):
        sum += -1 if nums[i] == 0 else 1
        if sum in sumToIndex:
            res = max(res, i - sumToIndex[sum])
        if sum not in sumToIndex:
            sumToIndex[sum] = i
    return res


for nums in [
    [0, 1],
    [0, 1, 0],
    [1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
