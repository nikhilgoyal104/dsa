from math import inf


# T=2ⁿ,S=n
def x(nums, profits, total):
    n = len(nums)

    def dfs(start, sum):
        if sum > total:
            return -inf
        res = 0
        for i in range(start, n):
            res = max(res, profits[i] + dfs(i + 1, sum + nums[i]))
        return res

    return dfs(0, 0)


# T=2ⁿ,S=n
def y(nums, profits, total):
    n = len(nums)

    def dfs(i, sum):
        if sum > total:
            return -inf
        if i == n or sum == total:
            return 0
        return max(profits[i] + dfs(i + 1, sum + nums[i]), dfs(i + 1, sum))

    return dfs(0, 0)


# T=ns,S=ns
# dp[i][j] = max profit for capacity j from the first i elements
def z(nums, profits, total):
    n = len(nums)
    dp = [[0] * (total + 1) for _ in range(n)]
    for j in range(total + 1):
        dp[0][j] = profits[0] if nums[0] <= j else 0
    for i in range(n):
        dp[i][0] = 0
    for i in range(1, n):
        for j in range(1, total + 1):
            dp[i][j] = max(dp[i - 1][j], (profits[i] + dp[i - 1][j - nums[i]]) if j >= nums[i] else 0)
    return dp[-1][-1]


for nums, profits, total in [
    ([4, 5, 3, 7], [2, 3, 1, 4], 5),
    ([1, 2, 3, 5], [1, 6, 10, 16], 5),
    ([1, 2, 3, 5], [1, 6, 10, 16], 6),
    ([1, 2, 3, 5], [1, 6, 10, 16], 7),
]:
    print(x(nums, profits, total), end=' ')
    print(y(nums, profits, total), end=' ')
    print(z(nums, profits, total))
