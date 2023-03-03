inputs = [
    [1],
    [2, 4],
    [2, 1, 5, 6, 2, 3],
    [2, 1, 5, 5, 5, 3],
    [6, 2, 5, 4, 5, 1, 6],
    [1, 1, 2, 3, 4, 4, 4, 4],
    [4, 4, 4, 4, 1, 1, 2, 3],
    [1, 1, 2, 3, 4, 4, 4, 4]
]


# T=n³,S=1
def main(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        minHeight = nums[i]
        for j in range(i, n):
            for k in range(i, j + 1):
                minHeight = min(minHeight, nums[k])
            res = max(res, minHeight * (j - i + 1))
    return res


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=n²,S=1
def main(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        minHeight = nums[i]
        for j in range(i, n):
            minHeight = min(minHeight, nums[j])
            res = max(res, minHeight * (j - i + 1))
    return res


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=n,S=n
# left[i] = index of next smaller element on left of nums[i]
# right[i] = index of next smaller element on right of nums[i]
def main(nums):
    n = len(nums)
    left = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    right = [n] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            right[stack.pop()] = i
        stack.append(i)
    res = 0
    for i in range(n):
        width = right[i] - left[i] - 1
        res = max(res, nums[i] * width)
    return res


for nums in inputs:
    print(main(nums), end=' ')
