from math import inf


def clean(nums):
    i, n, res = 0, len(nums), []
    while i < n:
        res.append(nums[i])
        while i + 1 < n and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return res


# LIS(nums) = LCS(nums,removeDuplicates(sorted(nums)))
# T=n²,S=n²
def w(nums):
    nums1, nums2 = nums, clean(sorted(nums))
    m, n = len(nums1), len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


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
    [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
    [8, 1, 6, 2, 3, 10],
    [10, 22, 9, 33, 21, 50, 41, 60, 80, 1],
    [10, 9, 2, 5, 3, 7, 101, 18],
    [7, 7, 7, 7, 7, 7, 7],
    [10, 9, 2, 5, 3, 7],
    [4, 10, 4, 3, 8, 9],
    [0, 1, 0, 3, 2, 3],
    [1, 2, 3]
]:
    print(w(nums), end=' ')
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
