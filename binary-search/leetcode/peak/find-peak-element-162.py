def main(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid + 1] > nums[mid]:
            low = mid + 1
        elif nums[mid - 1] > nums[mid]:
            high = mid
        else:
            return mid
    return low


for nums in [
    [1, 2, 3, 1],
    [1, 2, 1, 3, 5, 6, 4],
    [1],
    [1, 2],
    [2, 1],
    [1, 2, 1],
    [1, 2, 3],
    [1, 2, 3, 4, 7, 3, 2, 1, 0]
]:
    print(str(nums) + '->' + str(main(nums)))
