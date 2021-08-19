def x(nums, target):
    low, high = 0, len(nums) - 1
    while low < high:
        sum = nums[low] + nums[high]
        if target == sum:
            return [low + 1, high + 1]
        if target > sum:
            low += 1
        else:
            high -= 1


for nums, target in [
    ([2, 7, 11, 15], 9),
    ([2, 3, 4], 6),
    ([-1, 0], -1)
]:
    print(x(nums, target))
