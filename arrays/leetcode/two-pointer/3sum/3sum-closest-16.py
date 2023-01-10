from math import inf


# T=n²,S=1
def main(nums, target):
    n = len(nums)
    nums, res = sorted(nums), inf
    for i in range(n - 2):
        low, high = i + 1, n - 1
        while low < high:
            sum = nums[i] + nums[low] + nums[high]
            if abs(target - sum) < abs(target - res):
                res = sum
            if sum == target:
                return sum
            if sum > target:
                high -= 1
            else:
                low += 1
    return res


for nums, target in [
    ([1, 1, 1, 0], -100),
    ([-1, 2, 1, -4], 1),
    ([0, 0, 0], 1),
]:
    print(main(nums, target))
