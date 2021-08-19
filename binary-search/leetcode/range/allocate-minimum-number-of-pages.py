from math import inf


# T=nᵐ,S=n
def x(nums, m):
    def dfs(nums, m):
        if m == 1:
            return sum(nums)
        res = inf
        for i in range(1, len(nums) - m + 2):
            left, right = sum(nums[:i]), dfs(nums[i:], m - 1)
            res = min(res, max(left, right))
        return res

    return dfs(nums, m)


# T=n²m,S=nm
def y(nums, m):
    dp = {}

    def dfs(nums, m):
        if m == 1:
            return sum(nums)
        key = tuple(nums), m
        if key in dp:
            return dp[key]
        dp[key] = inf
        for i in range(1, len(nums) - m + 2):
            left, right = sum(nums[:i]), dfs(nums[i:], m - 1)
            dp[key] = min(dp[key], max(left, right))
        return dp[key]

    return dfs(nums, m)


# T=nlog(sum),S=1
def z(nums, m):
    def count(mid):
        sum, count = 0, 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum > mid:
                sum, count = nums[i], count + 1
        return count

    low, high = max(nums), sum(nums)
    while low <= high:
        mid = low + (high - low) // 2
        if count(mid) <= m:
            high = mid - 1
        else:
            low = mid + 1
    return low


for nums, m in [
    ([20, 10, 30, 40], 1),
    ([20, 10, 30, 40], 2),
    ([20, 10, 30, 40], 3),
    ([12, 34, 67, 90], 2),
    ([13, 43, 65, 87, 92], 2)
]:
    print(x(nums, m), end=' ')
    print(y(nums, m), end=' ')
    print(z(nums, m))
