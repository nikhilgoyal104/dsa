def x(nums, tar, vis):
    if not tar:
        return 1
    if tar < 0:
        return 0
    count = 0
    for val in nums:
        if val not in vis:
            vis.add(val)
            count += x(nums, tar - val, vis)
            vis.remove(val)
    return count


for nums, tar in [
    ([2, 3, 5, 6, 7], 12),
]:
    print(x(nums, tar, set()))


def y(nums, tar, vis):
    if not tar:
        return [[]]
    if tar < 0:
        return []
    res = []
    for val in nums:
        if val not in vis:
            vis.add(val)
            for path in y(nums, tar - val, vis):
                res.append([val] + path)
            vis.remove(val)
    return res


for nums, tar in [
    ([2, 3, 5, 6, 7], 12),
]:
    print(y(nums, tar, set()))
