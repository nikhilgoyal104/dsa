from math import inf


# T=n²,S=1
def main(nums):
    res, n = 0, len(nums)
    for i in range(n):
        minEle, maxEle, vis = inf, -inf, set()
        for j in range(i, n):
            if nums[j] in vis:
                break
            vis.add(nums[j])
            minEle = min(minEle, nums[j])
            maxEle = max(maxEle, nums[j])
            if maxEle - minEle == j - i:
                res = max(res, j - i + 1)
    return res


for nums in [
    [],
    [5],
    [1, 2, 3],
    [10, 12, 11],
    [14, 12, 11, 20],
    [1, 56, 58, 57, 90, 92, 94, 93, 91, 45],
    [10, 12, 12, 10, 10, 11, 10],
    [9, 2, 7, 5, 6, 23, 24, 22, 23, 19, 17, 16, 18, 39, 0]
]:
    print(main(nums))
