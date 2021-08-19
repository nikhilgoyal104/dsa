from math import inf


# T=n
def x(nums, tar):
    return min(nums, key=lambda val: abs(val - tar))


# T=n
def y(nums, tar):
    prev = -inf
    for val in nums:
        if prev <= tar < val:
            return min(prev, val, key=lambda val: abs(val - tar))
        prev = val
    return prev


# T=logn
def z(nums, tar):
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if tar == nums[mid]:
            return nums[mid]
        elif tar > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return n if low == n else min(nums[high], nums[low], key=lambda val: abs(val - tar))


for nums, tar in [
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
    print(x(nums, tar), end=' ')
    print(y(nums, tar), end=' ')
    print(z(nums, tar))
