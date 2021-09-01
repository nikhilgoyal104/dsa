# T=n²,S=1
def x(nums, k):
    res, n = 0, len(nums)
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum == k:
                res = max(res, j - i + 1)
    return res


# T=n,S=n
def y(nums, k):
    res, n = 0, len(nums)
    sum, sumToIndex = 0, {0: -1}
    for i in range(n):
        sum += nums[i]
        if sum - k in sumToIndex:
            res = max(res, i - sumToIndex[sum - k])
        if sum not in sumToIndex:
            sumToIndex[sum] = i
    return res


for nums, k in [
    ([10, 5, 2, 7, 1, 9], 15),
    ([-5, 8, -14, 2, 4, 12], -5),
    ([1, -1, 5, -2, 3], 3),
    ([-2, -1, 2, 1], 1)
]:
    print(x(nums, k), end=' ')
    print(y(nums, k))
