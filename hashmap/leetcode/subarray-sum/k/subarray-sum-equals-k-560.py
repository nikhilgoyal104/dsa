# T=n²,S=1
def x(nums, k):
    res, n = 0, len(nums)
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum == k:
                res += 1
    return res


# T=n,S=n
def y(nums, k):
    res, n = 0, len(nums)
    sum, sumFreq = 0, {0: 1}
    for i in range(n):
        sum += nums[i]
        if sum - k in sumFreq:
            res += sumFreq[sum - k]
        sumFreq[sum] = sumFreq.get(sum, 0) + 1
    return res


for nums, k in [
    ([10, 5, 2, 7, 1, 9], 15),
    ([-5, 8, -14, 2, 4, 12], -5),
    ([3, 9, -2, 4, 1, -7, 2, 6, -5, 8, -3, -7, 6, 2, 1], 5)
]:
    print(x(nums, k), end=' ')
    print(y(nums, k))
