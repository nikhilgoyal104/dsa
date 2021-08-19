def x(nums, tar):
    low, high = 0, len(nums) - 1
    while low < high:
        sum = nums[low] + nums[high]
        if tar == sum:
            return [low + 1, high + 1]
        if tar > sum:
            low += 1
        else:
            high -= 1


for nums, tar in [
    ([2, 7, 11, 15], 9),
    ([2, 3, 4], 6),
    ([-1, 0], -1)
]:
    print(x(nums, tar))
