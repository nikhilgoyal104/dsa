from collections import Counter


# T=n²,S=1
def x(nums):
    n = len(nums)
    res = 0
    for left in range(n):
        sum = 0
        for right in range(left, n):
            sum += -1 if not nums[right] else 1
            if not sum:
                res = max(res, right - left + 1)
    return res


# T=n,S=n
def y(nums):
    res = sum = 0
    sumToIndex = {0: -1}
    for right in range(len(nums)):
        sum += -1 if not nums[right] else 1
        if sum in sumToIndex:
            res = max(res, right - sumToIndex[sum])
        if sum not in sumToIndex:
            sumToIndex[sum] = right
    return res


for nums in [
    [0, 1],
    [0, 1, 0],
    [1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1]
]:
    print(x(nums), end=' ')
    print(y(nums))
