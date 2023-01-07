# T=n,S=1
def main(nums, k):
    res = left = zeros = 0
    for right in range(len(nums)):
        zeros += (nums[right] == 0)
        while zeros > k:
            zeros -= (nums[left] == 0)
            left += 1
        res = max(res, right - left + 1)
    return res


for nums, k in [
    ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2),
    ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3),
    ([1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1], 2)
]:
    print(main(nums, k))
