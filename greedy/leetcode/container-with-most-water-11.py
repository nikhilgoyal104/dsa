# T=n²,S=1
def x(nums):
    res, n = 0, len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            res = max(res, (j - i) * min(nums[i], nums[j]))
    return res


# T=n,S=1
def y(nums):
    low, high = 0, len(nums) - 1
    res = 0
    while low < high:
        res = max(res, (high - low) * min(nums[low], nums[high]))
        if nums[low] < nums[high]:
            low += 1
        else:
            high -= 1
    return res


for nums in [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [4, 3, 2, 1, 4],
    [1, 2, 1],
    [1, 1]
]:
    print(x(nums), end=' ')
    print(y(nums))
