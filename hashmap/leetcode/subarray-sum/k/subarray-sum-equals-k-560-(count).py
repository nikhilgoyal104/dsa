from collections import Counter


# T=n²,S=1
def x(nums, k):
    n = len(nums)
    res = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum == k:
                res += 1
    return res


# T=n,S=n
def y(nums, k):
    res = sum = 0
    sumFreq = Counter({0: 1})
    for i in range(len(nums)):
        sum += nums[i]
        res += sumFreq[sum - k]
        sumFreq[sum] += 1
    return res


for nums, k in [
    ([1, 1, 1], 2),
    ([1, 2, 3], 3),
    ([10, 5, 2, 7, 1, 9], 15),
    ([-5, 8, -14, 2, 4, 12], -5),
    ([3, 9, -2, 4, 1, -7, 2, 6, -5, 8, -3, -7, 6, 2, 1], 5)
]:
    print(x(nums, k), end=' ')
    print(y(nums, k))
