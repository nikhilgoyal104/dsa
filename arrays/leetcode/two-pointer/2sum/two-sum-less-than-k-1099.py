from math import inf


# T=nlogn,S=1
def main(nums, k):
    res, n = -inf, len(nums)
    nums = sorted(nums)
    low, high = 0, n - 1
    while low < high:
        sum = nums[low] + nums[high]
        if sum < k:
            res = max(res, sum)
            low += 1
        else:
            high -= 1
    return res if res != -inf else -1


for nums, k in [
    ([34, 23, 1, 24, 75, 33, 54, 8], 60),
    ([10, 20, 30], 15)
]:
    print(main(nums, k))
