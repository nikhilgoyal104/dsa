from math import inf


# T=n²,S=1
def x(nums):
    res, n = -inf, len(nums)
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            res = max(res, prod)
    return res


# T=n,S=1
def y(nums):
    res, n = -inf, len(nums)
    prod = 1
    for i in range(n):
        prod *= nums[i]
        res = max(res, prod)
        if prod == 0:
            prod = 1
    prod = 1
    for i in range(n - 1, -1, -1):
        prod *= nums[i]
        res = max(res, prod)
        if prod == 0:
            prod = 1
    return res


for nums in [
    [-2],
    [2, 3, -2, 4],
    [-2, 0, -1],
    [-3, 0, 1, -2],
    [2, -10, 3, 0, -9, -4, 19, 8, 0, 5]
]:
    print(x(nums), end=' ')
    print(y(nums))
