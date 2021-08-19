def pivot(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] < nums[high]:
            high = mid
        elif nums[mid] > nums[high]:
            low = mid + 1
        else:
            if nums[high - 1] > nums[high]:
                low = high
                break
            high -= 1
    return low


def search(low, high, nums, tar):
    while low <= high:
        mid = low + (high - low) // 2
        if tar == nums[mid]:
            return True
        elif tar > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


def x(nums, tar):
    n, pi = len(nums), pivot(nums)
    if nums[pi] == tar:
        return True
    return True if search(0, pi - 1, nums, tar) else search(pi + 1, n - 1, nums, tar)


for nums, tar in [
    ([2, 5, 6, 0, 0, 1, 2], 0),
    ([2, 5, 6, 0, 0, 1, 2], 3),
    ([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2])
]:
    print(x(nums, tar), end=' ')
