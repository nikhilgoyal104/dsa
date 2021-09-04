# T=n,S=1
def x(nums):
    n = len(nums)
    res = i = 0
    while i < n:
        count = int(nums[i] == 1)
        while i + 1 < n and nums[i] == nums[i + 1] == 1:
            count += 1
            i += 1
        res = max(res, count)
        i += 1
    return res


# T=n,S=1
def y(nums):
    for val in nums:
        pass


for nums in [
    [1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 0, 0],
    [0],
    [1],
]:
    print(x(nums), end=' ')
    print(y(nums))
