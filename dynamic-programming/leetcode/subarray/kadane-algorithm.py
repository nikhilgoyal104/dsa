inputs = [
    [0],
    [1],
    [5, 4, -1, 7, 8],
    [-2, -3, 4, -1, -2, 1, 5, -3],
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [-3, -2, -1],
    [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7],
    [4, 3, -2, 6, -14, 7, -1, 4, 5, 7, -10, 2, 9, -10, -5, -9, 6, 1],
    [4, 3, -2, 6, 7, -10, -10, 4, 5, 9, -3, 4, 7, -28, 2, 9, 3, 2, 11]
]


def x(nums):
    res = float('-inf')
    sum = 0
    for val in nums:
        sum += val
        if sum < val:
            sum = val
        res = max(res, sum)
    return res


for nums in inputs:
    print(x(nums), end=' ')

print('\n')


def y(nums):
    n = len(nums)
    res = float('-inf')
    sum = start = end = 0
    for i in range(n):
        sum += nums[i]
        if sum < nums[i]:
            start = i
            sum = nums[i]
        if sum > res:
            end = i
            res = sum
    return res, start, end


for nums in inputs:
    print(y(nums))

print()


def z(nums):
    res = float('-inf')
    sum = 0
    for val in nums:
        sum = max(sum + val, val)
        res = max(res, sum)
    return res


for nums in inputs:
    print(z(nums), end=' ')
