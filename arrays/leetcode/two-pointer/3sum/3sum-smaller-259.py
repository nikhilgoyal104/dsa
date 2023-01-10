# T=n²,S=1
def main(nums, target):
    res, n = 0, len(nums)
    nums = sorted(nums)
    for i in range(n - 2):
        low, high = i + 1, n - 1
        while low < high:
            sum = nums[i] + nums[low] + nums[high]
            if sum < target:
                res += high - low
                low += 1
            else:
                high -= 1
    return res


for nums, target in [
    ([-2, 0, 1, 3], 2),
    ([], 0),
    ([0], 0)
]:
    print(main(nums, target))
