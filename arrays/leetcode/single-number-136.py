from collections import Counter


# T=n,S=n
def x(nums):
    freq = Counter(nums)
    for key, val in freq.items():
        if val == 1:
            return key


# T=n,S=n
def y(nums):
    return 2 * sum(set(nums)) - sum(nums)


# T=n,S=1
def z(nums):
    res = 0
    for val in nums:
        res ^= val
    return res


for nums in [
    [2, 2, 1],
    [4, 1, 2, 1, 2]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
