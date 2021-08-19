from math import inf

tests = [
    [1],
    [5, 4, -1, 7, 8],
    [-2, -3, 4, -1, -2, 1, 5, -3],
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7],
    [4, 3, -2, 6, -14, 7, -1, 4, 5, 7, -10, 2, 9, -10, -5, -9, 6, 1],
    [4, 3, -2, 6, 7, -10, -10, 4, 5, 9, -3, 4, 7, -28, 2, 9, 3, 2, 11]
]


def w(nums):
    n, res, maxSum = len(nums), nums[0], nums[0]
    for i in range(1, n):
        if maxSum >= 0:
            maxSum += nums[i]
        else:
            maxSum = nums[i]
        if maxSum > res:
            res = maxSum
    return res


for nums in tests:
    print(w(nums), end=' ')

print('\n')


def x(nums):
    n, res, maxSum = len(nums), nums[0], nums[0]
    start = end = 0
    for i in range(1, n):
        if maxSum >= 0:
            maxSum += nums[i]
        else:
            start, maxSum = i, nums[i]
        if maxSum > res:
            res, end = maxSum, i
    return res, start, end


for nums in tests:
    print(x(nums))

print()


def y(nums):
    n, res, maxSum = len(nums), nums[0], nums[0]
    for i in range(1, n):
        maxSum = max(maxSum + nums[i], nums[i])
        res = max(res, maxSum)
    return res


for nums in tests:
    print(y(nums), end=' ')

print()


def z(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
    return max(dp)


for nums in tests:
    print(z(nums), end=' ')
