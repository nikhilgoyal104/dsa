# T=mn,S=mn
def x(nums1, nums2):
    m, n, dp = len(nums1), len(nums2), {}

    def dfs(i, j, count):
        if i == m or j == n:
            return count
        key = i, j, count
        if key in dp:
            return dp[key]
        if nums1[i] == nums2[j]:
            count = dfs(i + 1, j + 1, count + 1)
        dp[key] = max(count, dfs(i + 1, j, 0), dfs(i, j + 1, 0))
        return dp[key]

    return dfs(0, 0, 0)


# T=mn,S=mn
# dp[i][j] = longest common suffix of nums1[:i] and nums2[:j]
def y(nums1, nums2):
    m, n = len(nums1), len(nums2)
    res, dp = 0, [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                res = max(res, dp[i][j])
    return res


for nums1, nums2 in [
    ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
    ([83, 83, 83, 83, 83, 51, 47, 29, 7, 39],
     [93, 33, 31, 83, 83, 83, 83, 83, 92, 49])
]:
    print(x(nums1, nums2), end=' ')
    print(y(nums1, nums2))
