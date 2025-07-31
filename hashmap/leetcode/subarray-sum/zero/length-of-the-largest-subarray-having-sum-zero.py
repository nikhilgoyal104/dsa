# T=n²,S=1
def x(nums):
    n = len(nums)
    res = 0
    for left in range(n):
        sum = 0
        for right in range(left, n):
            sum += nums[right]
            if not sum:
                res = max(res, right - left + 1)
    return res


# T=n,S=n
def y(nums):
    res = sum = 0
    sumToIndex = {0: -1}
    for right in range(len(nums)):
        sum += nums[right]
        if sum in sumToIndex:
            res = max(res, right - sumToIndex[sum])
        if sum not in sumToIndex:
            sumToIndex[sum] = right
    return res


# T=n,S=n
def z(nums):
    res = sum = 0
    sumToIndex = {}
    for right in range(len(nums)):
        sum += nums[right]
        if sum == 0:
            res = right + 1
        if sum in sumToIndex:
            res = max(res, right - sumToIndex[sum])
        if sum not in sumToIndex:
            sumToIndex[sum] = right
    return res


for nums in [
    [0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0],
    [2, 8, -3, -5, 2, -4, 6, 1, 2, 1, -3, 4],
    [2, 3, 4, -4, -3, -2, 1, 2, 3],
    [15, -2, 2, -8, 1, 7, 10, 23],
    [1, 2, 3, 0],
    [1, 2, 3],
    [1, 0, 3],
    [0, 1, 2],
    [1, 2, 0],
    [2, 4, -2, -4, 5],
    [2, 4, -2, -4, 5, 9, 2, 1, 3, 5, -5, -2, -1, -3]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
