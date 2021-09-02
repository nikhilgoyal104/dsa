from math import inf


# T=n²,S=1
def main(nums):
    res, n = 1, len(nums)
    for i in range(n):
        minEle, maxEle = inf, -inf
        for j in range(i, n):
            minEle = min(minEle, nums[j])
            maxEle = max(maxEle, nums[j])
            if maxEle - minEle == j - i:
                res = max(res, j - i + 1)
    return res


for nums in [
    [1, 2, 3],
    [10, 12, 11],
    [14, 12, 11, 20],
    [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
]:
    print(main(nums))
