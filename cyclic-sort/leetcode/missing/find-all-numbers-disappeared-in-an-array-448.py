# T=n,S=n
def x(nums):
    return list(set(range(1, len(nums) + 1)) - set(nums))


# T=n,S=1
def y(nums):
    res = []
    n = len(nums)
    presentIndex = 0
    while presentIndex < n:
        correctIndex = nums[presentIndex] - 1
        if -1 < correctIndex < n and nums[presentIndex] != nums[correctIndex]:
            nums[correctIndex], nums[presentIndex] = nums[presentIndex], nums[correctIndex]
        else:
            presentIndex += 1
    for presentIndex in range(n):
        if presentIndex != nums[presentIndex] - 1:
            res.append(presentIndex + 1)
    return res


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
