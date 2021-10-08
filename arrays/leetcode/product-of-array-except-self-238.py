# T=n,S=n
def x(nums):
    n = len(nums)
    res, left, right = [1] * n, [1] * n, [1] * n
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
    for i in range(n):
        res[i] = left[i] * right[i]
    return res


# T=n,S=1
def y(nums):
    n = len(nums)
    res = [1] * n
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res


for nums in [
    [-1, 1, 0, -3, 3],
    [4, 5, 1, 8, 2],
    [1, 2, 3, 4]
]:
    print(x(nums))
    print(y(nums))
