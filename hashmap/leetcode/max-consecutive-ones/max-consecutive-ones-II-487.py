from collections import Counter


# T=n,S=1
def main(nums):
    n = len(nums)
    res = j = zeros = 0
    for i in range(n):
        zeros += nums[i] == 0
        while zeros > 1:
            zeros -= nums[j] == 0
            j += 1
        res = max(res, i - j + 1)
    return res


for nums in [
    [1],
    [0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 1]
]:
    print(main(nums))
