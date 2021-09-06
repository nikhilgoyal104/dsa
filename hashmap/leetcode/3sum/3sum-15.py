# T=n²,S=n
def main(nums):
    n = len(nums)
    res, nums = [], sorted(nums)
    for i in range(n):
        if nums[i] > 0:
            break
        if i and nums[i] == nums[i - 1]:
            continue
        twoSum(i, nums, res)
    return res


def twoSum(i, nums, res):
    low, high = i + 1, len(nums) - 1
    while low < high:
        sum = nums[i] + nums[low] + nums[high]
        if sum < 0:
            low += 1
        elif sum > 0:
            high -= 1
        else:
            res.append([nums[i], nums[low], nums[high]])
            low += 1
            high -= 1
            while low < high and nums[low] == nums[low - 1]:
                low += 1


for nums in [
    [-4, 2, 2, 2, 2],
    [-1, 0, 1, 2, -1, -4],
    [0],
    [],
]:
    print(main(nums))
