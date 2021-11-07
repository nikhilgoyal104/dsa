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


def search(low, high, nums, target):
    while low <= high:
        mid = low + (high - low) // 2
        if target == nums[mid]:
            return True
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


# T=logn,S=1
def main(nums, target):
    n, pi = len(nums), pivot(nums)
    if nums[pi] == target:
        return True
    return True if search(0, pi - 1, nums, target) else search(pi + 1, n - 1, nums, target)


for nums, target in [
    ([2, 5, 6, 0, 0, 1, 2], 0),
    ([2, 5, 6, 0, 0, 1, 2], 3),
    ([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2])
]:
    print(main(nums, target), end=' ')
