def reverse(nums, i):
    low, high = i, len(nums) - 1
    while low < high:
        nums[low], nums[high] = nums[high], nums[low]
        low, high = low + 1, high - 1


# T=n,S=1
def main(nums):
    n = len(nums)
    i = n - 1
    while i >= 1 and nums[i - 1] >= nums[i]:
        i -= 1
    if i:
        j = i
        while j < n and nums[j] > nums[i - 1]:
            j += 1
        nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
    reverse(nums, i)
    return nums


for nums in [
    [1, 2],
    [1, 2, 3],
    [3, 2, 1],
    [1, 1, 5],
    [1],
    [1, 5, 1],
    [1, 2, 3, 5, 4, 2],
    [1, 1],
    [5, 1, 1],
    [2, 3, 1, 3, 3],
    [4, 7, 6, 5, 5, 5, 3, 2, 1],
    [4, 7, 6, 5, 5, 5, 4, 4, 4, 3, 2, 1],
    [6, 2, 1, 5, 4, 3, 0],
    [6, 2, 3, 5, 4, 1, 0],
    [9, 5, 4, 3, 1]
]:
    print(str(nums) + ' -> ' + str(main(nums)))
