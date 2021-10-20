# T=ns,S=ns
def main(nums, total):
    n, dp = len(nums), {}

    def dfs(i, sum):
        if i == n:
            return int(sum == total)
        key = i, sum
        if key in dp:
            return dp[key]
        dp[key] = dfs(i + 1, sum + nums[i]) + dfs(i + 1, sum - nums[i])
        return dp[key]

    return dfs(0, 0)


for nums, total in [
    ([1, 1, 1, 1, 1], 3),
    ([1, 0], 1),
    ([1], 1)
]:
    print(main(nums, total))
