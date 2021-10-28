def main(nums):
    n, dp = len(nums), {}

    def dfs(i, stock, k):
        if i == n or k == 0:
            return 0
        key = i, stock, k
        if key in dp:
            return dp[key]
        if stock:
            dp[key] = max(dfs(i + 1, False, k - 1) + nums[i], dfs(i + 1, stock, k))
        else:
            dp[key] = max(dfs(i + 1, True, k) - nums[i], dfs(i + 1, stock, k))
        return dp[key]

    return dfs(0, False, 2)


for nums in [
    [3, 3, 5, 0, 0, 3, 1, 4],
    [1, 2, 3, 4, 5],
    [7, 6, 4, 3, 1],
    [1]
]:
    print(main(nums))
