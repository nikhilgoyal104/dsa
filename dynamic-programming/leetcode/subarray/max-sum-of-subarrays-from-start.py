from math import inf


# T=n,S=1
def x(nums):
    n = len(nums)
    res, sum = -inf, 0
    for i in range(n):
        sum += nums[i]
        res = max(res, sum)
    return res


for nums in [
    [1],
    [-1, -2, -3],
    [5, 4, -1, 7, 8],
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
]:
    print(x(nums))
