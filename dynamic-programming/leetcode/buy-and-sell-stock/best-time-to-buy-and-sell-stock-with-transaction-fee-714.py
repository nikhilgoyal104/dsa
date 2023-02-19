# T=n,S=n
def main(nums, fee):
    n = len(nums)
    dp = {}

    def dfs(i, bought):
        if i == n:
            return 0
        key = i, bought
        if key in dp:
            return dp[key]
        nothing = dfs(i + 1, bought)
        if bought:
            sell = dfs(i + 1, False) + nums[i] - fee
            dp[key] = max(sell, nothing)
            return dp[key]
        buy = dfs(i + 1, True) - nums[i]
        dp[key] = max(buy, nothing)
        return dp[key]

    return dfs(0, False)


for nums, fee in [
    ([1, 3, 2, 8, 4, 9], 2),
    ([1, 3, 7, 5, 10, 3], 3)
]:
    print(main(nums, fee))
