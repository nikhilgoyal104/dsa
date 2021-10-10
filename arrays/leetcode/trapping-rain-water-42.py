# T=n,S=n
# left[i] = max till i from left
# right[i] = max till i from right
def main(nums):
    n = len(nums)
    if n in [0, 1, 2]:
        return 0
    left, right = [0] * n, [0] * n
    left[0], right[-1] = nums[0], nums[-1]
    for i in range(1, n):
        left[i] = max(left[i - 1], nums[i])
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], nums[i])
    res = 0
    for i in range(1, n - 1):
        res += min(left[i], right[i]) - nums[i]
    return res


for nums in [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [4, 2, 0, 3, 2, 5],
    [3, 0, 0, 2, 0, 4],
    []
]:
    print(main(nums))
