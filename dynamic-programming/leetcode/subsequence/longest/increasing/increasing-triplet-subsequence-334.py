from math import inf


# T=n²,S=n
# dp[i] length of LIS ending with nums[i]
def x(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        dp[i] = 1 + max((dp[j] for j in range(i) if nums[j] < nums[i]), default=0)
        if dp[i] == 3:
            return True
    return False


# T=n,S=n
def y(nums):
    n = len(nums)
    if n < 3:
        return False
    stack, minSoFar, maxSoFarRight = [], nums[0], [0] * n
    maxSoFarRight[-1] = nums[-1]
    for k in range(n - 2, 1, -1):
        maxSoFarRight[k] = max(maxSoFarRight[k + 1], nums[k])
    for j in range(1, n - 1):
        if minSoFar < nums[j] < maxSoFarRight[j + 1]:
            return True
        minSoFar = min(minSoFar, nums[j])
    return False


# T=n,S=1
def z(nums):
    left, mid = inf, inf
    for right in nums:
        if right > mid:
            return True
        elif left < right < mid:
            mid = right
        elif right < left:
            left = right
    return False


for nums in [
    [5, 1, 6],
    [1, 3, 0, 5],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [5, 1, 5, 5, 0, 8],
    [2, 1, 5, 0, 4, 6],
    [5, 2, 4, 1, 5, 2, 2],
    [20, 100, 10, 12, 5, 13]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
