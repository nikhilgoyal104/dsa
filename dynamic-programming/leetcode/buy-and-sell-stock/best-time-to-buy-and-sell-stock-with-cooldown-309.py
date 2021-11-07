def main(nums):
    n, dp = len(nums), {}

    def dfs(i, stock):
        if i >= n:
            return 0
        key = i, stock
        if key in dp:
            return dp[key]
        if stock:
            dp[key] = max(dfs(i + 2, False) + nums[i], dfs(i + 1, stock))
        else:
            dp[key] = max(dfs(i + 1, True) - nums[i], dfs(i + 1, stock))
        return dp[key]

    return dfs(0, False)


for nums in [
    [1, 2, 3, 0, 2],
    [1]
]:
    print(main(nums))
