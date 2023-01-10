# T=n³,S=n
def x(nums, target):
    n = len(nums)
    res, nums = set(), sorted(nums)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            low, high = j + 1, n - 1
            while low < high:
                sum = nums[i] + nums[j] + nums[low] + nums[high]
                if sum == target:
                    res.add((nums[i], nums[j], nums[low], nums[high]))
                    low, high = low + 1, high - 1
                elif sum > target:
                    high -= 1
                else:
                    low += 1
    return list(map(list, res))


# T=n³,S=n
def y(nums, target):
    n = len(nums)
    res, nums = [], sorted(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            low, high = j + 1, n - 1
            while low < high:
                sum = nums[i] + nums[j] + nums[low] + nums[high]
                if sum == target:
                    res.append([nums[i], nums[j], nums[low], nums[high]])
                    low, high = low + 1, high - 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                elif sum > target:
                    high -= 1
                else:
                    low += 1
    return res


for nums, target in [
    ([1, 0, -1, 0, -2, 2], 0),
    ([2, 2, 2, 2, 2], 8),
    ([1, -2, -5, -4, -3, 3, 3, 5], -11),
]:
    print(x(nums, target))
    print(y(nums, target))
    print()
