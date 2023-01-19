from math import inf


# T=n
def x(nums, target):
    return min(nums, key=lambda val: abs(val - target))


# T=n
def y(nums, target):
    prev = -inf
    for val in nums:
        if prev <= target < val:
            return min(prev, val, key=lambda val: abs(val - target))
        prev = val
    return prev


# T=logn
def z(nums, target):
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target == nums[mid]:
            return nums[mid]
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return n if low == n else min(nums[high], nums[low], key=lambda val: abs(val - target))


for nums, target in [
    ([1], -4.2),
    ([1], 1),
    ([1], 2.4),
    ([1, 2, 3, 4, 5], 1),
    ([1, 2, 3, 4, 5], 2.36),
    ([1, 2, 3, 4, 5], 2.54),
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5], -4.25),
    ([1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 4, 5], 5.72),
]:
    print(x(nums, target), end=' ')
    print(y(nums, target), end=' ')
    print(z(nums, target))
