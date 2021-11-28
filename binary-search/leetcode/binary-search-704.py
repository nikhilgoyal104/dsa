# T=logn,S=1
def main(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


for nums, target in [
    ([-1, 0, 3, 5, 9, 12], 9),
    ([-1, 0, 3, 5, 9, 12], 2),
    ([4, 5], 2),
    ([4, 5], 8),
    ([5], 2),
    ([5], 5),
]:
    print(main(nums, target))
