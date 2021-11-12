# T=ns,S=s
def main(nums, total):
    dp = {total: 1}

    def dfs(sum):
        if sum > total:
            return 0
        if sum in dp:
            return dp[sum]
        dp[sum] = 0
        for val in nums:
            dp[sum] += dfs(sum + val)
        return dp[sum]

    return dfs(0)


for nums, total in [
    ([1, 2, 3], 4),
    ([9], 3)
]:
    print(main(nums, total))
