from math import inf

inputs = [
    [10, 15, 20],
    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
]


# T=2ⁿ,S=n
def main(nums):
    n = len(nums)

    def dfs(i):
        if i == n:
            return 0
        if i > n:
            return inf
        res = inf
        for jump in [1, 2]:
            res = min(res, nums[i] + dfs(i + jump))
        return res

    return min(dfs(i) for i in [0, 1])


for nums in inputs:
    print(main(nums))


# T=n,S=n
def main(nums):
    n = len(nums)
    dp = {n: 0}

    def dfs(i):
        if i in dp:
            return dp[i]
        if i > n:
            return inf
        dp[i] = inf
        for jump in [1, 2]:
            dp[i] = min(dp[i], nums[i] + dfs(i + jump))
        return dp[i]

    return min(dfs(i) for i in [0, 1])


for nums in inputs:
    print(main(nums))


# T=n,S=n
def main(nums):
    n = len(nums)

    def dfs(i):
        if i in [0, 1]:
            return 0
        if i < 0:
            return inf
        res = inf
        for jump in [1, 2]:
            res = min(res, nums[i - jump] + dfs(i - jump))
        return res

    return dfs(n)


for nums in inputs:
    print(main(nums))


# T=n,S=n
def main(nums):
    n = len(nums)
    dp = {0: 0, 1: 0}

    def dfs(i):
        if i in dp:
            return dp[i]
        if i < 0:
            return inf
        dp[i] = inf
        for jump in [1, 2]:
            dp[i] = min(dp[i], nums[i - jump] + dfs(i - jump))
        return dp[i]

    return dfs(n)


for nums in inputs:
    print(main(nums))


# T=n,S=n
def main(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 0
    for i in range(2, n + 1):
        dp[i] = min(nums[i - 1] + dp[i - 1], nums[i - 2] + dp[i - 2])
    return dp[-1]


for nums in inputs:
    print(main(nums))
