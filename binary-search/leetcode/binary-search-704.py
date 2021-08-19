def x(nums, tar):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if tar == nums[mid]:
            return mid
        elif tar > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


for nums, tar in [
    ([-1, 0, 3, 5, 9, 12], 9),
    ([-1, 0, 3, 5, 9, 12], 2),
    ([4, 5], 2),
    ([4, 5], 8),
    ([5], 2),
    ([5], 5),
]:
    print(x(nums, tar))
