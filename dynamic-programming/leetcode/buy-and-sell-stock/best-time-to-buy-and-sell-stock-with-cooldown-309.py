# T=n,S=n
def main(nums):
    n = len(nums)
    dp = {}

    def dfs(i, bought):
        if i >= n:
            return 0
        key = i, bought
        if key in dp:
            return dp[key]
        nothing = dfs(i + 1, bought)
        if bought:
            sell = dfs(i + 2, False) + nums[i]
            dp[key] = max(sell, nothing)
            return dp[key]
        buy = dfs(i + 1, True) - nums[i]
        dp[key] = max(buy, nothing)
        return dp[key]

    return dfs(0, False)


for nums in [
    [1, 2, 3, 0, 2],
    [1]
]:
    print(main(nums))
