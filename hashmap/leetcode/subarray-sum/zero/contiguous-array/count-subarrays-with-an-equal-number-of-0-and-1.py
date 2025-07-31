from collections import Counter


# T=n,S=n
def main(nums):
    res = sum = 0
    sumFreq = Counter({0: 1})
    for right in range(len(nums)):
        sum += 0 if not nums[right] else 1
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
