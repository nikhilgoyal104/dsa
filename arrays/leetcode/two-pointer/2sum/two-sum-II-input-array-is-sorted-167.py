# T=n,S=1
def main(nums, target):
    low, high = 0, len(nums) - 1
    while low < high:
        sum = nums[low] + nums[high]
        if sum == target:
            return [low + 1, high + 1]
        if sum > target:
            high -= 1
        else:
            low += 1


for nums, target in [
    ([2, 7, 11, 15], 9),
    ([2, 3, 4], 6),
    ([-1, 0], -1)
]:
    print(main(nums, target))
