inputs = [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [4, 2, 0, 3, 2, 5],
    [3, 0, 0, 2, 0, 4],
    [2, 0, 2]
]


# T=n²,S=1
def main(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        leftMax = rightMax = nums[i]
        for j in range(i):
            leftMax = max(leftMax, nums[j])
        for k in range(i + 1, n):
            rightMax = max(rightMax, nums[k])
        res += min(leftMax, rightMax) - nums[i]
    return res


for nums in inputs:
    print(main(nums), end=' ')

print()


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


for nums in inputs:
    print(main(nums), end=' ')
