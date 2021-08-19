# T=n,S=1
def x(nums):
    n = len(nums)
    for i in range(n):
        dest = nums[i] - 1
        while nums[i] != nums[dest]:
            nums[i], nums[dest] = nums[dest], nums[i]
            dest = nums[i] - 1
    return nums


# T=n,S=1
def y(nums):
    i, n = 0, len(nums)
    while i < n:
        dest = nums[i] - 1
        if nums[i] != nums[dest]:
            nums[i], nums[dest] = nums[dest], nums[i]
        else:
            i += 1
    return nums


for nums in [
    [],
    [1],
    [2, 1],
    [5, 4, 3, 2, 1],
    [3, 4, 6, 2, 1, 5],
    [4, 1, 3, 5, 6, 2],
    [2, 6, 4, 1, 3, 5]
]:
    print(x(nums), end=' ')
    print(y(nums))
