from math import inf
from collections import Counter


# T=n,S=n
def main(nums):
    res, count = inf, Counter(nums)
    degree = max(count.values())
    j, freq = 0, Counter()
    for i in range(len(nums)):
        freq[nums[i]] += 1
        while freq[nums[i]] == degree:
            res = min(res, i - j + 1)
            freq[nums[j]] -= 1
            j += 1
    return res


for nums in [
    [1, 2, 2, 3, 1],
    [1, 2, 2, 3, 1, 4, 2]
]:
    print(main(nums))
