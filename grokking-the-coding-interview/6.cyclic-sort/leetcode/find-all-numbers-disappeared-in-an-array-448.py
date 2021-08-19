# T=n,S=n
def x(nums):
    return list(set(range(1, len(nums) + 1)) - set(nums))


# T=n,S=1
def y(nums):
    n = len(nums)
    for i in range(n):
        dest = nums[i] - 1
        while nums[i] != nums[dest]:
            nums[i], nums[dest] = nums[dest], nums[i]
            dest = nums[i] - 1
    return [i + 1 for i in range(n) if i != nums[i] - 1]


for nums in [
    [2, 6, 4, 4, 3, 2],
    [3, 4, 4, 5, 5],
    [5, 4, 7, 2, 3, 5, 3],
    [2, 3, 1, 8, 2, 3, 5, 1],
    [2, 4, 1, 2],
    [2, 3, 1, 2],
    [4, 3, 2, 7, 8, 2, 3, 1],
    [1, 1]
]:
    print(x(nums), end=' ')
    print(y(nums))
