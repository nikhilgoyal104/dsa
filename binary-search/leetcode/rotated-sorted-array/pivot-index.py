def x(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] < nums[high]:
            high = mid
        elif nums[mid] > nums[high]:
            low = mid + 1
    return low


for nums in [
    [1],
    [1, 2],
    [2, 1],
    [3, 1],
    [1, 2, 3],
    [3, 1, 2],
    [2, 3, 1],
    [1, 2, 3, 4],
    [4, 1, 2, 3],
    [3, 4, 1, 2],
    [2, 3, 4, 1],
    [1, 2, 3, 4, 5],
    [5, 1, 2, 3, 4],
    [4, 5, 1, 2, 3],
    [3, 4, 5, 1, 2],
    [2, 3, 4, 5, 1],
    [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],
    [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
]:
    print(str(nums) + ' -> ' + str(x(nums)))
