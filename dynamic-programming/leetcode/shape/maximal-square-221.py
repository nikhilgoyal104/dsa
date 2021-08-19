from math import inf


def largestSquare(nums):
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
        width, height = right[i] - left[i] - 1, nums[i]
        if width >= height:
            res = max(res, height * height)
    return res


# T=mn,S=m
def x(grid):
    if not grid:
        return 0
    m, n, heights = len(grid), len(grid[0]), list(map(int, grid[0]))
    res = largestSquare(heights)
    for i in range(1, m):
        for j in range(n):
            heights[j] = int(heights[j]) + 1 if int(grid[i][j]) else 0
        res = max(res, largestSquare(heights))
    return res


# T=mn,S=mn
def y(grid):
    m, n, dp = len(grid), len(grid[0]), {}

    def dfs(ri, ci):
        if ri == m or ci == n or not int(grid[ri][ci]):
            return 0
        key = ri, ci
        if key in dp:
            return dp[key]
        dp[key] = inf
        for i, j in (0, 1), (1, 0), (1, 1):
            dp[key] = min(dp[key], 1 + dfs(ri + i, ci + j))
        return dp[key]

    return max((dfs(i, j) for i in range(m) for j in range(n) if int(grid[i][j])), default=0) ** 2


# T=mn,S=mn
def z(grid):
    m, n = len(grid), len(grid[0])
    dp, side = [[0] * n for _ in range(m)], 0
    for i in range(m):
        dp[i][-1], side = int(grid[i][-1]), max(side, int(grid[i][-1]))
    for j in range(n):
        dp[-1][j], side = int(grid[-1][j]), max(side, int(grid[-1][j]))
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            if int(grid[i][j]):
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
            side = max(side, dp[i][j])
    return side ** 2


for grid in [
    [
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0']
    ],
    [
        ['0', '1'],
        ['1', '0']
    ],
    [
        ['0']
    ]
]:
    print(x(grid), end=' ')
    print(y(grid), end=' ')
    print(z(grid))
