# T=ntar,S=total
def x(nums, total):
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


# T=ntar,S=total
def y(coins, n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for target in range(1, n + 1):
        for coin in coins:
            if target >= coin:
                dp[target] += dp[target - coin]
    return dp[-1]


for nums, total in [
    ([1, 2, 3], 4),
    ([9], 3)
]:
    print(x(nums, total), end=' ')
    print(y(nums, total))
