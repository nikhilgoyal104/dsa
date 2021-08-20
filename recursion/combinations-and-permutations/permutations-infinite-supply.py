def x(nums, total):
    def dfs(sum):
        if sum == total:
            return 1
        if sum > total:
            return 0
        res = 0
        for val in nums:
            res += dfs(sum + val)
        return res

    return dfs(0)


def y(nums, total):
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


for nums, total in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 11),
]:
    print(x(nums, total), end=' ')
    print(y(nums, total))

print()


def x(nums, total):
    def dfs(sum):
        if sum == total:
            return [[]]
        if sum > total:
            return []
        res = []
        for val in nums:
            for path in dfs(sum + val):
                res.append([val] + path)
        return res

    return dfs(0)


def y(nums, total):
    dp = {total: [[]]}

    def dfs(sum):
        if sum > total:
            return []
        if sum in dp:
            return dp[sum]
        dp[sum] = []
        for val in nums:
            for path in dfs(sum + val):
                dp[sum].append([val] + path)
        return dp[sum]

    return dfs(0)


for nums, total in [
    ([1, 2, 3], 4),
    ([2, 3, 5], 7),
]:
    print(x(nums, total))
    print(y(nums, total))
