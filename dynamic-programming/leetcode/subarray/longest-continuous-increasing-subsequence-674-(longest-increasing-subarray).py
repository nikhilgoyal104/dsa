# T=n²,S=1
def x(nums):
    n, res = len(nums), 1
    for i in range(n):
        j, size = i + 1, 1
        while j < n and nums[j - 1] < nums[j]:
            size, j = size + 1, j + 1
        res = max(res, size)
    return res


# T=n,S=1
def y(nums):
    n, i, res = len(nums), 0, 1
    while i < n:
        j, size = i + 1, 1
        while j < n and nums[j - 1] < nums[j]:
            j, size = j + 1, size + 1
        res, i = max(res, size), j
    return res


for nums in [
    [1, 3, 5, 4, 7],
    [2, 2, 2, 2, 2]
]:
    print(x(nums), end=' ')
    print(y(nums))
