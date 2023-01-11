from collections import Counter


# T=n,S=n
def main(nums):
    res, n = 0, len(nums)
    nums = [-1 if not val else 1 for val in nums]
    sum, sumFreq = 0, Counter({0: 1})
    for i in range(n):
        sum += nums[i]
        res += sumFreq[sum]
        sumFreq[sum] += 1
    return res


for nums in [
    [0, 1],
    [0, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1]
]:
    print(main(nums))
