def x(nums, total):
    if not total:
        return 1
    if total < 0:
        return 0
    count = 0
    for val in nums:
        count += x(nums, total - val)
    return count


def y(nums, total, dp):
    if total < 0:
        return 0
    if total in dp:
        return dp[total]
    dp[total] = 0
    for val in nums:
        dp[total] += y(nums, total - val, dp)
    return dp[total]


def z(coins, n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for target in range(1, n + 1):
        for coin in coins:
            if target >= coin:
                dp[target] += dp[target - coin]
    return dp[-1]


for nums, total in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 11),
]:
    print(x(nums, total), end=' ')
    print(y(nums, total, {0: 1}), end=' ')
    print(z(nums, total))

print()


def x(nums, total):
    if not total:
        return [[]]
    if total < 0:
        return []
    res = []
    for val in nums:
        for path in x(nums, total - val):
            res.append([val] + path)
    return res


def y(nums, total, dp):
    if not total:
        return [[]]
    if total < 0:
        return []
    if total in dp:
        return dp[total]
    dp[total] = []
    for val in nums:
        for path in y(nums, total - val, dp):
            dp[total].append([val] + path)
    return dp[total]


for nums, total in [
    ([1, 2, 3], 4),
    ([2, 3, 5], 7),
]:
    print(x(nums, total))
    print(y(nums, total, {}))
