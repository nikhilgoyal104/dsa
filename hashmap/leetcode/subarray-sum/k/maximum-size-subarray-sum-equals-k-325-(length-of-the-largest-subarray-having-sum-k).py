# T=n²,S=1
def x(nums, k):
    n = len(nums)
    res = 0
    for left in range(n):
        sum = 0
        for right in range(left, n):
            sum += nums[right]
            if sum == k:
                res = max(res, right - left + 1)
    return res


# T=n,S=n
def y(nums, k):
    res = sum = 0
    sumToIndex = {0: -1}
    for right in range(len(nums)):
        sum += nums[right]
        if sum - k in sumToIndex:
            res = max(res, right - sumToIndex[sum - k])
        if sum not in sumToIndex:
            sumToIndex[sum] = right
    return res


# T=n,S=n
def z(nums, k):
    res = sum = 0
    sumToIndex = {}
    for right in range(len(nums)):
        sum += nums[right]
        if sum == k:
            res = right + 1
        if sum - k in sumToIndex:
            res = max(res, right - sumToIndex[sum - k])
        if sum not in sumToIndex:
            sumToIndex[sum] = right
    return res


for nums, k in [
    ([10, 5, 2, 7, 1, 9], 15),
    ([-5, 8, -14, 2, 4, 12], -5),
    ([1, -1, 5, -2, 3], 3),
    ([-2, -1, 2, 1], 1)
]:
    print(x(nums, k), end=' ')
    print(y(nums, k), end=' ')
    print(z(nums, k))
