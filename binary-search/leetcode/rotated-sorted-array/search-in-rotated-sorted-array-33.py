def pivot(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] < nums[high]:
            high = mid
        elif nums[mid] > nums[high]:
            low = mid + 1
    return low


def search(low, high, nums, tar):
    while low <= high:
        mid = low + (high - low) // 2
        if tar == nums[mid]:
            return mid
        elif tar > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def x(nums, tar):
    n, pi = len(nums), pivot(nums)
    if nums[pi] == tar:
        return pi
    res = search(0, pi - 1, nums, tar)
    return res if res != -1 else search(pi + 1, n - 1, nums, tar)


for nums, tar in [
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([4, 5, 6, 7, 0, 1, 2], 3),
    ([1], 0),
    ([3, 1], 3)
]:
    print(x(nums, tar))
