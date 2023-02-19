# T=n²,S=1
def x(nums):
    n = len(nums)
    res = 1
    for i in range(n):
        j = i + 1
        size = 1
        while j < n and nums[j - 1] < nums[j]:
            size += 1
            j += 1
        res = max(res, size)
    return res


# T=n,S=1
def y(nums):
    n = len(nums)
    i = 0
    res = 1
    while i < n:
        j = i + 1
        size = 1
        while j < n and nums[j - 1] < nums[j]:
            size += 1
            j += 1
        res = max(res, size)
        i = j
    return res


for nums in [
    [1, 3, 5, 4, 7],
    [2, 2, 2, 2, 2]
]:
    print(x(nums), end=' ')
    print(y(nums))
