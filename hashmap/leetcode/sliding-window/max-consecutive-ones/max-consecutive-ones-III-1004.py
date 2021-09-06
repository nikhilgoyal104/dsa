from collections import Counter


# T=n,S=1
def main(nums, k):
    n = len(nums)
    res = j = zeros = 0
    for i in range(n):
        zeros += nums[i] == 0
        while zeros > k:
            zeros -= nums[j] == 0
            j += 1
        res = max(res, i - j + 1)
    return res


for nums, k in [
    ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2),
    ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3),
    ([1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1], 2)
]:
    print(main(nums, k))
