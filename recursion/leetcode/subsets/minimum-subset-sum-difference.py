# T=2ⁿ,S=n
def x(nums):
    n = len(nums)

    def dfs(i, sum1, sum2):
        if i == n:
            return abs(sum1 - sum2)
        return min(dfs(i + 1, sum1 + nums[i], sum2), dfs(i + 1, sum1, sum2 + nums[i]))

    return dfs(0, 0, 0)


# T=ns,S=ns
def y(nums):
    n, dp = len(nums), {}

    def dfs(i, sum1, sum2):
        if i == n:
            return abs(sum1 - sum2)
        key = i, sum1, sum2
        if key in dp:
            return dp[key]
        dp[key] = min(dfs(i + 1, sum1 + nums[i], sum2), dfs(i + 1, sum1, sum2 + nums[i]))
        return dp[key]

    return dfs(0, 0, 0)


for nums in [
    [1, 2, 3, 9],
    [1, 2, 7, 1, 5],
    [1, 3, 100, 4]
]:
    print(x(nums), end=' ')
    print(y(nums))
