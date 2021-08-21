def x(nums):
    nums.sort()
    n, stack = len(nums), [nums[0]]
    for i in range(1, n):
        curr, next = stack[-1], nums[i]
        if next[0] <= curr[1]:
            curr[1] = max(next[1], curr[1])
        else:
            stack.append(next)
    return stack


for nums in [
    [[1, 3], [2, 6], [8, 10], [15, 18]],
    [[1, 4], [4, 5]],
    [[1, 3], [2, 4], [5, 7], [6, 8]],
    [[1, 4], [2, 3]],
    [[10, 16], [2, 8], [1, 6], [7, 12]],
    [[1, 2], [2, 3], [3, 4], [1, 3]]
]:
    print(x(nums), end='')
    print()
