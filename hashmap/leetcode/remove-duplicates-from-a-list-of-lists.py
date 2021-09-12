def w(nums):
    res, nums = [], sorted(nums)
    for i in range(len(nums)):
        if i and nums[i] == nums[i - 1]:
            continue
        res.append(nums[i])
    return res


def x(nums):
    res, nums = [], sorted(nums)
    for i in range(len(nums)):
        if not i or nums[i] != nums[i - 1]:
            res.append(nums[i])
    return res


def y(nums):
    res = {tuple(val) for val in nums}
    return [list(val) for val in res]


def z(nums):
    res = set(map(tuple, nums))
    return list(map(list, res))


for nums in [
    [[1, 2], [4], [5, 6, 2], [1, 2], [3], [4]]
]:
    print(w(nums))
    print(x(nums))
    print(y(nums))
    print(z(nums))
