from collections import Counter


# T=n,S=k
def main(nums, k):
    res, n = 0, len(nums)
    sum, remainderFreq = 0, Counter({0: 1})
    for i in range(n):
        sum += nums[i]
        res += remainderFreq[sum % k]
        remainderFreq[sum % k] += 1
    return res


for nums, k in [
    ([2, 3, 5, 4, 5, 3, 4], 7),
    ([2, 7, 6, 1, 4, 5], 3),
    ([2, -6, 3, 1, 2, 8, 2, 1], 7),
    ([4, 5, 0, -2, -3, 1], 5),
    ([5], 9)
]:
    print(main(nums, k))
