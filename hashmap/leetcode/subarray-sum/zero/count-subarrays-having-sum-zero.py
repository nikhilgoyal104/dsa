from collections import Counter


# T=n²,S=1
def x(nums):
    n, res = len(nums), 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if not sum:
                res += 1
    return res


# T=n,S=n
def y(nums):
    res, n = 0, len(nums)
    sum, sumFreq = 0, Counter({0: 1})
    for i in range(n):
        sum += nums[i]
        res += sumFreq[sum]
        sumFreq[sum] += 1
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
]:
    print(x(nums), end=' ')
    print(y(nums))
