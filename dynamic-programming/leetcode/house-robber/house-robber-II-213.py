def x(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    def helper(nums):
        dp = {}

        def dfs(i):
            if i >= n - 1:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return dp[i]

        return dfs(0)

    return max(helper(nums[:n - 1]), helper(nums[1:]))


for nums in [
    [2, 3, 2], [1, 2, 3, 1], [0], [1], [1, 2]
]:
    print(x(nums))
