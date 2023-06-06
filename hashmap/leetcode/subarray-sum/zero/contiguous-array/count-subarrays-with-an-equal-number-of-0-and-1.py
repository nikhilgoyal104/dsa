from collections import Counter


# T=n,S=n
def main(nums):
    res = sum = 0
    sumFreq = Counter({0: 1})
    nums = [-1 if not val else 1 for val in nums]
    for i in range(len(nums)):
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
