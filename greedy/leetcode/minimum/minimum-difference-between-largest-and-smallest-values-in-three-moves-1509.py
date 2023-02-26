# T=nlogn
def main(nums):
    if len(nums) < 5:
        return 0
    nums = sorted(nums)
    return min(nums[i - 4] - nums[i] for i in range(4))


for nums in [
    [1, 3],
    [1, 3, 8],
    [5, 3, 2, 4],
    [1, 5, 0, 10, 14],
    [6, 6, 0, 1, 1, 4, 6]
]:
    print(main(nums))
