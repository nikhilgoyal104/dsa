from math import inf


def w(nums, total):
    n = len(nums)

    def dfs(i, sum):
        if sum > total:
            return -inf
        if sum == total or i == n:
            return 0
        inc = nums[i] + dfs(i + 1, sum + nums[i])
        exc = dfs(i + 1, sum)
        return max(inc, exc)

    return dfs(0, 0)


def x(nums, total):
    n, dp = len(nums), {}

    def dfs(i, sum):
        if sum > total:
            return -inf
        if sum == total or i == n:
            return 0
        key = i, sum
        if key in dp:
            return dp[key]
        inc = nums[i] + dfs(i + 1, sum + nums[i])
        exc = dfs(i + 1, sum)
        dp[key] = max(inc, exc)
        return dp[key]

    return dfs(0, 0)


def y(nums, total):
    n, dp = len(nums), {}

    def dfs(start, sum):
        if sum > total:
            return -inf
        key = start, sum
        if key in dp:
            return dp[key]
        dp[key] = 0
        for i in range(start, n):
            dp[key] = max(dp[key], nums[i] + dfs(i + 1, sum + nums[i]))
        return dp[key]

    return dfs(0, 0)


for nums, total in [
    ([1, 2, 3], 5),
    ([2, 5, 1, 3, 4], 7),
    ([1, 2, 3, 8, 7, 4], 10),
    ([1, 2, 3], 6),
    ([1, 2, 3], 10),
    ([7, 3, 5], 8)
]:
    print(x(nums, total), end=' ')
    print(y(nums, total))
