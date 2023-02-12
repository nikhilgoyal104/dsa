# T=nlogn
def x(nums):
    nums.sort()
    n, least, res = len(nums), float('inf'), []
    for i in range(n - 1):
        least = min(least, nums[i + 1] - nums[i])
    for i in range(n - 1):
        if nums[i + 1] - nums[i] == least:
            res.append([nums[i], nums[i + 1]])
    return res


# T=nlogn
def y(nums):
    nums.sort()
    n = len(nums)
    least = min(nums[i + 1] - nums[i] for i in range(n - 1))
    return [[nums[i], nums[i + 1]] for i in range(n - 1) if nums[i + 1] - nums[i] == least]


for nums in [
    [4, 2, 1, 3],
    [1, 3, 6, 10, 15],
    [3, 8, -10, 23, 19, -4, -14, 27]
]:
    print(x(nums))
    print(y(nums))
