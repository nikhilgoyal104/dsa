def x(nums, start, total):
    if not total:
        return 1
    if total < 0:
        return 0
    count = 0
    for i in range(start, len(nums)):
        count += x(nums, i, total - nums[i])
    return count


def y(nums, start, total, dp):
    if not total:
        return 1
    if total < 0:
        return 0
    key = start, total
    if key in dp:
        return dp[key]
    dp[key] = 0
    for i in range(start, len(nums)):
        dp[key] += y(nums, i, total - nums[i], dp)
    return dp[key]


def z(coins, n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for coin in coins:
        for target in range(coin, n + 1):
            dp[target] += dp[target - coin]
    return dp[-1]


for nums, total in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 11)
]:
    print(x(nums, 0, total), end=' ')
    print(y(nums, 0, total, {}), end=' ')
    print(z(nums, total))

print()


def x(nums, start, total):
    if not total:
        return [[]]
    if total < 0:
        return []
    res = []
    for i in range(start, len(nums)):
        for path in x(nums, i, total - nums[i]):
            res.append([nums[i]] + path)
    return res


def y(nums, start, total, dp):
    if not total:
        return [[]]
    if total < 0:
        return []
    key = start, total
    if key in dp:
        return dp[key]
    dp[key] = []
    for i in range(start, len(nums)):
        for path in y(nums, i, total - nums[i], dp):
            dp[key].append([nums[i]] + path)
    return dp[key]


for nums, total in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 11)
]:
    print(x(nums, 0, total))
    print(y(nums, 0, total, {}))
