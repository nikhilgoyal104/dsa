from collections import Counter


# T=n,S=n
def main(nums):
    remainders = [val % 60 for val in nums]
    res, freq = 0, Counter(remainders)
    for remainder in remainders:
        complement = 60 - remainder
        res += freq[complement] if remainder else freq[0]
        if remainder == complement or not remainder:
            res -= 1
    return res // 2


for nums in [
    [30, 20, 150, 100, 40],
    [60, 60, 60, 60],
    [60, 60, 60]
]:
    print(main(nums))
