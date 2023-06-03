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


# T=n²,S=1
def main(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        left = -1
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[i]:
                left = j
                break
        right = n
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                right = j
                break
        res = max(res, nums[i] * (right - left - 1))
    return res


for nums in inputs:
    print(main(nums), end=' ')

print()


def firstSmallerLeft(nums):
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(i)
    return res


def firstSmallerRight(nums):
    n = len(nums)
    res = [n] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            res[stack.pop()] = i
        stack.append(i)
    return res


# T=n,S=n
# left[i] = index of first smaller element on left of nums[i]
# right[i] = index of first smaller element on right of nums[i]
def main(nums):
    res = 0
    left = firstSmallerLeft(nums)
    right = firstSmallerRight(nums)
    for i in range(len(nums)):
        width = right[i] - left[i] - 1
        res = max(res, nums[i] * width)
    return res


for nums in inputs:
    print(main(nums), end=' ')
