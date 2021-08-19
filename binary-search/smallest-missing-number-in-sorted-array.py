# T=n
def x(nums):
    n = len(nums)
    for i in range(n):
        if i != nums[i]:
            return i
    return n


# T=logn
def y(nums):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] != mid:
            high = mid - 1
        else:
            low = mid + 1
    return low


for nums in [
    [0, 1, 2, 6, 9, 11, 15],
    [1, 2, 3, 4, 6, 9, 11, 15],
    [0, 1, 2, 3, 4, 5, 6]
]:
    print(x(nums), end=' ')
    print(y(nums))
