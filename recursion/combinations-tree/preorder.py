def x(nums, i, start):
    print(nums[i] if i != -1 else None, end=' ')
    for i in range(start, len(nums)):
        x(nums, i, i + 1)


for nums in [
    [1, 2, 3],
    [1, 2, 3, 4]
]:
    x(nums, -1, 0)
    print()
