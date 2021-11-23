# T=n,S=n
# left[i] = index of first smaller element on left of nums[i]
# right[i] = index of first smaller element on right of nums[i]
def largestRectangle(nums):
    n = len(nums)
    stack, left = [], [-1] * n
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    stack, right = [], [n] * n
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            right[stack.pop()] = i
        stack.append(i)
    res = 0
    for i in range(n):
        width = right[i] - left[i] - 1
        res = max(res, nums[i] * width)
    return res


# T=mn,S=m
def main(grid):
    if not grid:
        return 0
    m, n, heights = len(grid), len(grid[0]), list(map(int, grid[0]))
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
