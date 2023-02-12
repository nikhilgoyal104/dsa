# T=n,S=n
def main(nums):
    n = len(nums)
    res = 0
    leftMax = [0] * n
    leftMax[0] = nums[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], nums[i])
    rightMax = [0] * n
    rightMax[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], nums[i])
    for i in range(1, n - 1):
        res += min(leftMax[i], rightMax[i]) - nums[i]
    return res


for nums in [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [3, 0, 0, 2, 0, 4]
]:
    print(main(nums))
