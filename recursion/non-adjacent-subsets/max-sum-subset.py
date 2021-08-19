from math import inf


def x(nums):
    n = len(nums)

    def dfs(i, sum):
        if i >= n:
            return sum
        return max(dfs(i + 2, sum + nums[i]), dfs(i + 1, sum))

    return dfs(0, 0)


def y(nums):
    n, res = len(nums), [0]

    def dfs(start, sum):
        res[0] = max(res[0], sum)
        for i in range(start, n):
            dfs(i + 2, sum + nums[i])

    dfs(0, 0)
    return res[0]


for nums in [
    [1, 2, 3],
    [1, 2, 3, 1],
    [2, 7, 9, 3, 1]
]:
    print(x(nums), end=' ')
    print(y(nums))

print()


def x(nums):
    n, dp = len(nums), {}

    def dfs(i, sum):
        if i >= n:
            return sum
        key = i, sum
        if key in dp:
            return dp[key]
        dp[key] = max(dfs(i + 2, sum + nums[i]), dfs(i + 1, sum))
        return dp[key]

    return dfs(0, 0)


def y(nums):
    n, res, dp = len(nums), [0], {}

    def dfs(start, sum):
        key = start, sum
        if key in dp:
            return
        res[0] = max(res[0], sum)
        dp[key] = res[0]
        for i in range(start, n):
            dfs(i + 2, sum + nums[i])

    dfs(0, 0)
    return res[0]


for nums in [
    [1, 2, 3],
    [1, 2, 3, 1],
    [2, 7, 9, 3, 1],
    [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81,
     185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211],
    [169, 44, 4, 44, 181, 35, 115, 220, 121, 24, 194, 195, 188, 180, 27, 241, 5, 195, 140, 148, 218, 78, 73, 201, 26,
     217, 183, 226, 204, 172, 109, 27, 44, 69, 27, 159, 224, 177, 41, 15, 80, 89, 102, 4, 40, 114, 177, 145, 154, 46,
     120, 3, 25, 47, 92, 194, 173, 168, 137, 203, 121, 44, 59, 215, 142, 71, 214, 144, 220, 212, 9, 38, 248, 219, 32, 6,
     18, 182, 174]
]:
    print(x(nums), end=' ')
    print(y(nums))
