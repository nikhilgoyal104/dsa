# T=n,S=1
def main(nums):
    n = len(nums)
    res = float('-inf')
    sum = 0
    for i in range(n):
        sum += nums[i]
    res = max(res, sum)
    return res


for nums in [
    [1],
    [-1, -2, -3],
    [5, 4, -1, 7, 8],
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
]:
    print(main(nums))
