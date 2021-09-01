# T=n²,S=1
def x(nums):
    n, res = len(nums), 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if not sum:
                res = max(res, j - i + 1)
    return res


# T=n,S=n
def y(nums):
    res, n = 0, len(nums)
    sum, prefixSumToIndex = 0, {0: -1}
    for i in range(n):
        sum += nums[i]
        if sum in prefixSumToIndex:
            res = max(res, i - prefixSumToIndex[sum])
        else:
            prefixSumToIndex[sum] = i
    return res


for nums in [
    [15, -2, 2, -8, 1, 7, 10, 23],
    [2, 3, 4, -4, -3, -2, 1, 2, 3],
    [1, 2, 3],
    [1, 0, 3]
]:
    print(x(nums), end=' ')
    print(y(nums))
