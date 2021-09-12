# T=n²,S=n
def x(nums):
    n = len(nums)
    res, nums = set(), sorted(nums)
    for i in range(n - 2):
        low, high = i + 1, n - 1
        while low < high:
            sum = nums[i] + nums[low] + nums[high]
            if sum == 0:
                res.add((nums[i], nums[low], nums[high]))
                low, high = low + 1, high - 1
            elif sum > 0:
                high -= 1
            else:
                low += 1
    return list(map(list, res))


# T=n²,S=n
def y(nums):
    n = len(nums)
    res, nums = [], sorted(nums)
    for i in range(n - 2):
        if i and nums[i] == nums[i - 1]:
            continue
        low, high = i + 1, n - 1
        while low < high:
            sum = nums[i] + nums[low] + nums[high]
            if sum == 0:
                res.append([nums[i], nums[low], nums[high]])
                low, high = low + 1, high - 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
            elif sum > 0:
                high -= 1
            else:
                low += 1
    return res


for nums in [
    [-4, 2, 2, 2, 2],
    [-1, 0, 1, 2, -1, -4],
    [0],
    [],
]:
    print(x(nums))
    print(y(nums))
    print()
