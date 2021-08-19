# T=n,S=n
def x(nums):
    n = len(nums)
    if n in [0, 1, 2]:
        return 0
    maxSoFarLeft, maxSoFarRight = [0] * n, [0] * n
    maxSoFarLeft[0], maxSoFarRight[-1] = nums[0], nums[-1]
    for i in range(1, n):
        maxSoFarLeft[i] = max(maxSoFarLeft[i - 1], nums[i])
    for i in range(n - 2, -1, -1):
        maxSoFarRight[i] = max(maxSoFarRight[i + 1], nums[i])
    res = 0
    for i in range(1, n - 1):
        res += min(maxSoFarLeft[i], maxSoFarRight[i]) - nums[i]
    return res


for nums in [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [4, 2, 0, 3, 2, 5],
    [3, 0, 0, 2, 0, 4],
    []
]:
    print(x(nums))
