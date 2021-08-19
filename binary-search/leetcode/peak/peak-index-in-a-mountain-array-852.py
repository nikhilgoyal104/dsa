# T=n,S=1
def x(nums):
    for i in range(1, len(nums) - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return i
    return -1


# T=logn,S=1
def y(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid + 1] > nums[mid]:
            low = mid + 1
        elif nums[mid - 1] > nums[mid]:
            high = mid
        else:
            return mid
    return -1


for nums in [
    [1, 2, 3, 4],
    [0, 1, 0],
    [0, 2, 1, 0],
    [0, 10, 5, 2],
    [3, 4, 5, 1],
    [24, 69, 100, 99, 79, 78, 67, 36, 26, 19],
]:
    print(x(nums), end=' ')
    print(y(nums))
