inputs = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [4, 3, 2, 1, 4],
    [1, 2, 1],
    [1, 1]
]


# T=n²,S=1
def main(nums):
    n = len(nums)
    res = 0
    for left in range(n):
        for right in range(left + 1, n):
            area = min(nums[left], nums[right]) * (right - left)
            res = max(res, area)
    return res


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=n,S=1
def main(nums):
    res = left = 0
    right = len(nums) - 1
    while left < right:
        area = min(nums[left], nums[right]) * (right - left)
        res = max(res, area)
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return res


for nums in inputs:
    print(main(nums), end=' ')
