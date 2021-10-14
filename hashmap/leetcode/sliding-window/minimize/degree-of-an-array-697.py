from math import inf
from collections import Counter


# T=n,S=n
def main(nums):
    res, n = inf, len(nums)
    degree = max(Counter(nums).values())
    left, freq = 0, Counter()
    for right in range(n):
        freq[nums[right]] += 1
        while freq[nums[right]] == degree:
            res = min(res, right - left + 1)
            freq[nums[left]] -= 1
            left += 1
    return res


for nums in [
    [1, 2, 2, 3, 1],
    [1, 2, 2, 3, 1, 4, 2],
    [1, 3, 2, 4, 2, 3, 4, 2, 5, 6, 5, 5, 7]
]:
    print(main(nums))
