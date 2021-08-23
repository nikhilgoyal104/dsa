from math import inf


# T=2ⁿ,S=n
def x(nums):
    n = len(nums)

    def dfs(i, prev):
        if i == n:
            return 0
        inc = 1 + dfs(i + 1, nums[i]) if prev < nums[i] else 0
        return max(inc, dfs(i + 1, prev))

    return dfs(0, -inf)


# T=2ⁿ,S=n
def y(nums):
    n = len(nums)

    def dfs(start, prev):
        res = 0
        for i in range(start, n):
            if prev < nums[i]:
                res = max(res, 1 + dfs(i + 1, nums[i]))
        return res

    return dfs(0, -inf)


# T=n²,S=n
# dp[i] length of LIS ending with nums[i]
def z(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)


for nums in [
    [8, 1, 6, 2, 3, 10],
    [10, 22, 9, 33, 21, 50, 41, 60, 80, 1],
    [10, 9, 2, 5, 3, 7, 101, 18],
    [7, 7, 7, 7, 7, 7, 7],
    [10, 9, 2, 5, 3, 7],
    [4, 10, 4, 3, 8, 9],
    [0, 1, 0, 3, 2, 3],
    [1, 2, 3]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
