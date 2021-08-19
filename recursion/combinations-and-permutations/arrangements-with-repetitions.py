def x(nums, tar):
    if not tar:
        return 1
    if tar < 0:
        return 0
    count = 0
    for val in nums:
        count += x(nums, tar - val)
    return count


def y(nums, tar, dp):
    if tar < 0:
        return 0
    if tar in dp:
        return dp[tar]
    dp[tar] = 0
    for val in nums:
        dp[tar] += y(nums, tar - val, dp)
    return dp[tar]


def z(coins, n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for target in range(1, n + 1):
        for coin in coins:
            if target >= coin:
                dp[target] += dp[target - coin]
    return dp[-1]


for nums, tar in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 11),
]:
    print(x(nums, tar), end=' ')
    print(y(nums, tar, {0: 1}), end=' ')
    print(z(nums, tar))

print()


def x(nums, tar):
    if not tar:
        return [[]]
    if tar < 0:
        return []
    res = []
    for val in nums:
        for path in x(nums, tar - val):
            res.append([val] + path)
    return res


def y(nums, tar, dp):
    if not tar:
        return [[]]
    if tar < 0:
        return []
    if tar in dp:
        return dp[tar]
    dp[tar] = []
    for val in nums:
        for path in y(nums, tar - val, dp):
            dp[tar].append([val] + path)
    return dp[tar]


for nums, tar in [
    ([1, 2, 3], 4),
    ([2, 3, 5], 7),
]:
    print(x(nums, tar))
    print(y(nums, tar, {}))
