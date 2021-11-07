def main(nums, fee):
    n, dp = len(nums), {}

    def dfs(i, stock):
        if i == n:
            return 0
        key = i, stock
        if key in dp:
            return dp[key]
        if stock:
            dp[key] = max(dfs(i + 1, False) + nums[i] - fee, dfs(i + 1, stock))
        else:
            dp[key] = max(dfs(i + 1, True) - nums[i], dfs(i + 1, stock))
        return dp[key]

    return dfs(0, False)


for nums, fee in [
    ([1, 3, 2, 8, 4, 9], 2),
    ([1, 3, 7, 5, 10, 3], 3)
]:
    print(main(nums, fee))
