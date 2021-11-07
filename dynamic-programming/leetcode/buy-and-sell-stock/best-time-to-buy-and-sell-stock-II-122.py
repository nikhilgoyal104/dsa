def main(nums):
    n, dp = len(nums), {}

    def dfs(i, stock):
        if i == n:
            return 0
        key = i, stock
        if key in dp:
            return dp[key]
        if stock:
            dp[key] = max(dfs(i + 1, False) + nums[i], dfs(i + 1, stock))
        else:
            dp[key] = max(dfs(i + 1, True) - nums[i], dfs(i + 1, stock))
        return dp[key]

    return dfs(0, False)


for nums in [
    [7, 1, 5, 3, 6, 4],
    [1, 2, 3, 4, 5],
    [7, 6, 4, 3, 1]
]:
    print(main(nums))
