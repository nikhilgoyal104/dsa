# T=logn,S=1
def main(nums):
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
    return nums[low]


for nums in [
    [1, 1, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 1, 2, 1],
    [1, 3, 5],
    [2, 2, 2, 0, 1],
    [1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 2, 1, 1]
]:
    print(main(nums))
