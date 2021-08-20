# T=ns,S=ns
def x(nums):
    if sum(nums) % 2:
        return False
    n, total, dp = len(nums), sum(nums) // 2, {}

    def dfs(start, sum):
        if sum == total:
            return True
        if sum > total:
            return False
        key = start, sum
        if key in dp:
            return dp[key]
        for i in range(start, n):
            if dfs(i + 1, sum + nums[i]):
                dp[key] = True
                return dp[key]
        dp[key] = False
        return dp[key]

    return dfs(0, 0)


# T=ns,S=ns
def y(nums):
    if sum(nums) % 2:
        return False
    n, total, dp = len(nums), sum(nums) // 2, {}

    def dfs(i, sum):
        if sum == total:
            return True
        if sum > total or i == n:
            return False
        key = i, sum
        if key in dp:
            return dp[key]
        dp[key] = dfs(i + 1, sum + nums[i]) or dfs(i + 1, sum)
        return dp[key]

    return dfs(0, 0)


# T=ns,S=ns
# dp[i][j] = is sum of numbers till index i equal to j
def z(nums):
    if sum(nums) % 2:
        return False
    n, total = len(nums), sum(nums) // 2
    dp = [[False] * (total + 1) for _ in range(n)]
    for j in range(total + 1):
        dp[0][j] = nums[0] == j
    for i in range(n):
        dp[i][0] = True
    for i in range(1, n):
        for j in range(1, total + 1):
            dp[i][j] = dp[i - 1][j] or (j >= nums[i] and dp[i - 1][j - nums[i]])
    return dp[-1][-1]


for nums in [
    [1, 2, 5],
    [1, 5, 11, 5],
    [1, 2, 3, 5],
    [2, 2, 3, 5],
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 97]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
