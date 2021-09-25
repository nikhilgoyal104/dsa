from math import inf
from collections import Counter


# T=n,S=n
def main(nums):
    res, n = inf, len(nums)
    degree = max(Counter(nums).values())
    j, freq = 0, Counter()
    for i in range(n):
        freq[nums[i]] += 1
        while freq[nums[i]] == degree:
            res = min(res, i - j + 1)
            freq[nums[j]] -= 1
            j += 1
    return res


for nums in [
    [1, 2, 2, 3, 1],
    [1, 2, 2, 3, 1, 4, 2],
    [1, 3, 2, 4, 2, 3, 4, 2, 5, 6, 5, 5, 7]
]:
    print(main(nums))
