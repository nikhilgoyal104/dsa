def pivot(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] < nums[high]:
            high = mid
        elif nums[mid] > nums[high]:
            low = mid + 1
    return low


def search(low, high, nums, target):
    while low <= high:
        mid = low + (high - low) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# T=logn,S=1
def main(nums, target):
    n, pi = len(nums), pivot(nums)
    if nums[pi] == target:
        return pi
    res = search(0, pi - 1, nums, target)
    return res if res != -1 else search(pi + 1, n - 1, nums, target)


for nums, target in [
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([4, 5, 6, 7, 0, 1, 2], 3),
    ([1], 0),
    ([3, 1], 3)
]:
    print(main(nums, target))
