from statistics import median


def x(nums):
    nums.sort()
    n = len(nums)
    i = n // 2
    if n % 2 == 1:
        return nums[i]
    return (nums[i - 1] + nums[i]) / 2


def y(nums):
    return median(nums)


for nums in [
    [1],
    [1, 2],
    [1, 3, 4, 2, 6, 5, 8, 7],
    [4, 4, 4, 4, 4],
    [2, 4, 5, 6, 7, 8, 9, ]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print()
