# T=nxsum,S=nxsum
def x(nums):
    total = sum(nums)
    if total % 2:
        return False
    n, tar, dp = len(nums), total // 2, {}

    def dfs(start, sum):
        if sum == tar:
            return True
        if sum > tar:
            return False
        key = start, sum
        if key in dp:
            return dp[key]
        dp[key] = False
        for i in range(start, n):
            if dfs(i + 1, sum + nums[i]):
                dp[key] = True
                return dp[key]
        return dp[key]

    return dfs(0, 0)


# T=nxsum,S=nxsum
def y(nums):
    total = sum(nums)
    if total % 2:
        return False
    n, tar, dp = len(nums), total // 2, {}

    def dfs(i, sum):
        if sum == tar:
            return True
        if sum > tar or i == n:
            return False
        key = i, sum
        if key in dp:
            return dp[key]
        dp[key] = dfs(i + 1, sum + nums[i]) or dfs(i + 1, sum)
        return dp[key]

    return dfs(0, 0)


# T=nxsum,S=nxsum
# dp[i][j] = is sum of numbers till index i = j+1
def z(nums):
    total = sum(nums)
    if total % 2:
        return False
    n, tar = len(nums), total // 2
    rows, cols = n, tar
    dp = [[False for _ in range(cols)] for _ in range(rows)]
    for j in range(cols):
        dp[0][j] = j + 1 == nums[0]
    for i in range(1, rows):
        for j in range(cols):
            dp[i][j] = dp[i - 1][j] or (dp[i - 1][j - nums[i]] if j - nums[i] >= 0 else False)
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
