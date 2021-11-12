# T=n,S=1
def main(nums):
    n = len(nums)
    for i in range(n):
        dest = nums[i] - 1
        while 1 <= nums[i] <= n and nums[i] != nums[dest]:
            nums[i], nums[dest] = nums[dest], nums[i]
            dest = nums[i] - 1
    for i in range(n):
        if i != nums[i] - 1:
            return i + 1
    return n + 1


for nums in [
    [3, 2, 4, 6, 1],
    [1, 2, 4, 3],
    [2, 1, 3]
]:
    print(main(nums))
