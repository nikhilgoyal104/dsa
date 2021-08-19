def x(nums, start, k):
    if not k:
        return [[]]
    res = []
    for i in range(start, len(nums)):
        for path in x(nums, i + 1, k - 1):
            res.append([nums[i]] + path)
    return res


for nums, k in [
    ([1, 2, 3], 2),
    ([1, 2, 3, 4], 2)
]:
    print(x(nums, 0, k))
