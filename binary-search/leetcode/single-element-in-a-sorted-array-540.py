# T=n,S=1
def x(nums):
    res = 0
    for val in nums:
        res ^= val
    return res


# T=n,S=1
def y(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    i = 0
    while i < n - 1:
        if nums[i] != nums[i + 1]:
            return nums[i]
        i += 2
    return nums[i]


# T=logn,S=1
def z(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if mid % 2:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        else:
            high = mid
    return nums[low]


for nums in [
    [1, 2, 2, 3, 3, 4, 4],
    [1, 1, 2, 2, 3, 3, 4, 4, 5],
    [1, 1, 2, 3, 3, 4, 4, 8, 8],
    [3, 3, 7, 7, 10, 11, 11],
    [1, 1, 2, 2, 4, 6, 6, 8, 8, 9, 9],
    [1, 2, 2],
    [1, 1, 2],
    [1, 2, 2, 3, 3],
    [1, 1, 2, 2, 3],
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
