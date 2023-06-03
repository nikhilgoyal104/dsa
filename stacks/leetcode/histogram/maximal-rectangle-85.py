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
def largestRectangle(nums):
    left = firstSmallerLeft(nums)
    right = firstSmallerRight(nums)
    res = 0
    for i in range(len(nums)):
        width = right[i] - left[i] - 1
        res = max(res, nums[i] * width)
    return res


# T=mn,S=m
def main(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0]),
    heights = list(map(int, grid[0]))
    res = largestRectangle(heights)
    for i in range(1, m):
        for j in range(n):
            heights[j] = int(heights[j]) + 1 if int(grid[i][j]) else 0
        res = max(res, largestRectangle(heights))
    return res


for grid in [
    [
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0']
    ],
    [],
    [
        ['0']
    ],
    [
        ['1']
    ],
    [
        ['0', '0']
    ],
    [
        ['1', '0', '1', '1', '1']
    ]
]:
    print(main(grid))
