from math import inf


# T=n³,S=1
def x(nums):
    n, res = len(nums), -inf
    for i in range(n):
        for j in range(i, n):
            res = max(res, sum(nums[i:j + 1]))
    return res


# T=n²,S=1
def y(nums):
    n, res = len(nums), -inf
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            res = max(res, sum)
    return res


# T=n,S=1
def z(nums):
    sum, res = 0, -inf
    for val in nums:
        sum = max(sum + val, val)
        res = max(res, sum)
    return res


for nums in [
    [0],
    [1],
    [5, 4, -1, 7, 8],
    [-2, -3, 4, -1, -2, 1, 5, -3],
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [-3, -2, -1],
    [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7],
    [4, 3, -2, 6, -14, 7, -1, 4, 5, 7, -10, 2, 9, -10, -5, -9, 6, 1],
    [4, 3, -2, 6, 7, -10, -10, 4, 5, 9, -3, 4, 7, -28, 2, 9, 3, 2, 11]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
