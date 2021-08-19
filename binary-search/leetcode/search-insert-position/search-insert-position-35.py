# T=n,S=1
def x(nums, target):
    n = len(nums)
    for i in range(n):
        if target == nums[i] or target < nums[i]:
            return i
    return n


# T=logn,S=1
def y(nums, target):
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


for nums, target in [
    ([1, 3, 5, 6], 5),
    ([1, 3, 5, 6], 2),
    ([1, 3, 5, 6], 7),
    ([1, 3, 5, 6], 0),
    ([1], 0),
    ([1, 3], 2),
    ([1, 3], 1),
    ([1, 3], 3),
    ([1, 2, 3, 4, 5, 10], 2),
    ([10, 20, 30, 40, 50, 59], 45)
]:
    print(x(nums, target), end=' ')
    print(y(nums, target))
