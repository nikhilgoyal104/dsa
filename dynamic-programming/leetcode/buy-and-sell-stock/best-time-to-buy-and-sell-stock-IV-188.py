def main(k, nums):
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

    return dfs(0, False, k)


for k, nums in [
    (2, [2, 4, 1]), (2, [3, 2, 6, 5, 0, 3])
]:
    print((main(k, nums)))
