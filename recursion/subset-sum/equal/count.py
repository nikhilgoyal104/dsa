def x(nums, total):
    n = len(nums)

    def dfs(start, sum):
        if sum == total:
            return 1
        if sum > total:
            return 0
        res = 0
        for i in range(start, n):
            res += dfs(i + 1, sum + nums[i])
        return res

    return dfs(0, 0)


# T=2ⁿ,S=n
def y(nums, total):
    n = len(nums)

    def dfs(i, sum):
        if sum == total:
            return 1
        if sum > total or i == n:
            return 0
        inc = dfs(i + 1, sum + nums[i])
        exc = dfs(i + 1, sum)
        return inc + exc

    return dfs(0, 0)


# T=ns,S=ns
# dp[i][j] = number of ways of making sum j from numbers till index i
def z(nums, total):
    n = len(nums)
    dp = [[0] * (total + 1) for _ in range(n)]
    for j in range(total + 1):
        dp[0][j] = int(nums[0] == j)
    for i in range(n):
        dp[i][0] = 1
    for i in range(1, n):
        for j in range(1, total + 1):
            dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - nums[i]] if j >= nums[i] else 0)
    return dp[-1][-1]


for nums, total in [
    ([1, 2, 3], 5),
    ([2, 5, 1, 3, 4], 7),
    ([1, 2, 3, 8, 7, 4], 10),
    ([1, 1, 1, 1, 1], 4),
    ([1, 2, 3], 6),
    ([7, 3, 5], 8)
]:
    print(x(nums, total), end=' ')
    print(y(nums, total), end=' ')
    print(z(nums, total))
