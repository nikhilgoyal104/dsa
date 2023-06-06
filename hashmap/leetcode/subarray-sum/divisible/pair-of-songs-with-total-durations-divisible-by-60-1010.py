from collections import Counter


# T=n,S=n
def main(nums):
    res = 0
    remainders = [val % 60 for val in nums]
    remainderFreq = Counter(remainders)
    for remainder in remainders:
        complement = 60 - remainder
        res += remainderFreq[complement] if remainder else remainderFreq[0]
        if remainder == complement or not remainder:
            res -= 1
    return res // 2


for nums in [
    [30, 20, 150, 100, 40],
    [60, 60, 60, 60],
    [60, 60, 60]
]:
    print(main(nums))
