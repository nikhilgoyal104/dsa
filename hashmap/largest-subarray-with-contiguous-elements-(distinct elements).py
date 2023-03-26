# T=n²,S=1
def main(nums):
    n = len(nums)
    res = 1
    for i in range(n):
        minVal = float('inf')
        maxVal = float('-inf')
        for j in range(i, n):
            minVal = min(minVal, nums[j])
            maxVal = max(maxVal, nums[j])
            if maxVal - minVal == j - i:
                res = max(res, j - i + 1)
    return res


for nums in [
    [1, 2, 3],
    [10, 12, 11],
    [14, 12, 11, 20],
    [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
]:
    print(main(nums))
