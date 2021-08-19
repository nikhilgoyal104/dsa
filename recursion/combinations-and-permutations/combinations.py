def x(nums, start, tar):
    if not tar:
        return 1
    if tar < 0:
        return 0
    count = 0
    for i in range(start, len(nums)):
        count += x(nums, i + 1, tar - nums[i])
    return count


def y(nums, start, tar, dp):
    if not tar:
        return 1
    if tar < 0:
        return 0
    key = start, tar
    if key in dp:
        return dp[key]
    dp[key] = 0
    for i in range(start, len(nums)):
        dp[key] += y(nums, i + 1, tar - nums[i], dp)
    return dp[key]


for nums, tar in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 11)
]:
    print(x(nums, 0, tar), end=' ')
    print(y(nums, 0, tar, {}))

print()


def x(nums, start, tar):
    if not tar:
        return [[]]
    if tar < 0:
        return []
    res = []
    for i in range(start, len(nums)):
        for path in x(nums, i + 1, tar - nums[i]):
            res.append([nums[i]] + path)
    return res


def y(nums, start, tar, dp):
    if not tar:
        return [[]]
    if tar < 0:
        return []
    key = start, tar
    if key in dp:
        return dp[key]
    dp[key] = []
    for i in range(start, len(nums)):
        for path in y(nums, i + 1, tar - nums[i], dp):
            dp[key].append([nums[i]] + path)
    return dp[key]


for nums, tar in [
    ([1, 2, 3], 4),
    ([1, 2, 5], 11),
    ([4, 2, 7, 1, 3], 10)
]:
    print(x(nums, 0, tar))
    print(y(nums, 0, tar, {}))
