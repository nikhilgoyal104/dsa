def main(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target >= nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None if low == len(nums) else nums[low]


for (nums, target) in [
    ([1, 4, 7, 8, 8, 8, 8, 10, 12, 14, 16], 8),
    ([1, 2, 3, 5, 8, 12], 5),
    ([1, 2, 3, 5, 8, 12], 4),
    ([1, 2, 3, 5, 8, 12], 8),
    ([1, 2, 3, 5, 8, 12], 15),
    ([1, 2, 3, 5, 8, 12], -5)
]:
    print(main(nums, target))
