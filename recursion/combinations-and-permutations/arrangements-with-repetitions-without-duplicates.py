def x(nums, total, vis):
    if not total:
        return 1
    if total < 0:
        return 0
    count = 0
    for val in nums:
        if val not in vis:
            vis.add(val)
            count += x(nums, total - val, vis)
            vis.remove(val)
    return count


for nums, total in [
    ([2, 3, 5, 6, 7], 12),
]:
    print(x(nums, total, set()))


def y(nums, total, vis):
    if not total:
        return [[]]
    if total < 0:
        return []
    res = []
    for val in nums:
        if val not in vis:
            vis.add(val)
            for path in y(nums, total - val, vis):
                res.append([val] + path)
            vis.remove(val)
    return res


for nums, total in [
    ([2, 3, 5, 6, 7], 12),
]:
    print(y(nums, total, set()))
