from collections import Counter


# T=n,S=1
def main(nums):
    res = left = zeros = 0
    for right in range(len(nums)):
        zeros += (nums[right] == 0)
        while zeros > 1:
            zeros -= (nums[left] == 0)
            left += 1
        res = max(res, right - left + 1)
    return res


for nums in [
    [1],
    [0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 1]
]:
    print(main(nums))
