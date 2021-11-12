# T=n,S=1
def main(nums):
    n = len(nums)
    for i in range(n):
        dest = nums[i] - 1
        while nums[i] != nums[dest]:
            nums[i], nums[dest] = nums[dest], nums[i]
            dest = nums[i] - 1
    for i in range(n):
        if i != nums[i] - 1:
            return [nums[i], i + 1]


for nums in [
    [4, 3, 4, 5, 1],
    [4, 3, 5, 4, 1],
    [1, 2, 2, 4],
    [1, 1]
]:
    print(main(nums))
