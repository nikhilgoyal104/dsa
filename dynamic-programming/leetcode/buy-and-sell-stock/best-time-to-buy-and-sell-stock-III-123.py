# T=n,S=n
def main(nums):
    n = len(nums)
    dp = {}

    def dfs(i, bought, k):
        if i == n or k == 0:
            return 0
        key = i, bought, k
        if key in dp:
            return dp[key]
        nothing = dfs(i + 1, bought, k)
        if bought:
            sell = dfs(i + 1, False, k - 1) + nums[i]
            dp[key] = max(sell, nothing)
            return dp[key]
        buy = dfs(i + 1, True, k) - nums[i]
        dp[key] = max(buy, nothing)
        return dp[key]

    return dfs(0, False, 2)


for nums in [
    [3, 3, 5, 0, 0, 3, 1, 4],
    [1, 2, 3, 4, 5],
    [7, 6, 4, 3, 1],
    [1]
]:
    print(main(nums))
