from collections import Counter
from math import factorial as fact


def nCr(n, r):
    return fact(n) // (fact(n - r) * fact(r))


# T=n,S=1
def x(nums, target):
    res, freq = 0, Counter(nums)
    for val in freq:
        if val == target - val and freq[val] > 1:
            res += 2 * nCr(freq[val], 2)
        else:
            res += freq[val] * freq[target - val]
    return res // 2


# T=n,S=1
def y(nums, target):
    res, freq = 0, Counter(nums)
    for val in nums:
        res += freq[target - val]
        if val == target - val:
            res -= 1
    return res // 2


for nums, target in [
    ([3], 6),
    ([3, 3], 6),
    ([3, 3, 3, 3, 4, 2], 6),
    ([1, 5, 7, -1], 6),
    ([1, 5, 7, -1, 5], 6),
    ([1, 1, 1, 1], 2),
    ([10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1], 11)
]:
    print(x(nums, target), end=' ')
    print(y(nums, target))
