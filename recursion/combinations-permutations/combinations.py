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


def y(nums, total):
    n, dp = len(nums), {}

    def dfs(start, sum):
        if sum == total:
            return 1
        if sum > total:
            return 0
        key = start, sum
        if key in dp:
            return dp[key]
        dp[key] = 0
        for i in range(start, n):
            dp[key] += dfs(i + 1, sum + nums[i])
        return dp[key]

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
    ([1, 2, 3], 4),
    ([1, 2, 5], 11),
    ([4, 2, 7, 1, 3], 10)
]:
    print(x(nums, total), end=' ')
    print(y(nums, total), end=' ')
    print(z(nums, total))

print()


def x(nums, total):
    n = len(nums)

    def dfs(start, sum):
        if sum == total:
            return [[]]
        if sum > total:
            return []
        res = []
        for i in range(start, n):
            for path in dfs(i + 1, sum + nums[i]):
                res.append([nums[i]] + path)
        return res

    return dfs(0, 0)


def y(nums, total):
    n, dp = len(nums), {}

    def dfs(start, sum):
        if sum == total:
            return [[]]
        if sum > total:
            return []
        key = start, sum
        if key in dp:
            return dp[key]
        dp[key] = []
        for i in range(start, n):
            for path in dfs(i + 1, sum + nums[i]):
                dp[key].append([nums[i]] + path)
        return dp[key]

    return dfs(0, 0)


for nums, total in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 11),
    ([4, 2, 7, 1, 3], 10)
]:
    print(x(nums, total))
    print(y(nums, total))
