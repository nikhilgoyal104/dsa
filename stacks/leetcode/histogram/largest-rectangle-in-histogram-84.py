# T=n,S=n
# left[i] = index of first smaller element on left of nums[i]
# right[i] = index of first smaller element on right of nums[i]
def main(nums):
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


for nums in [
    [1, 1, 2, 3, 4, 4, 4, 4],
    [4, 4, 4, 4, 1, 1, 2, 3],
    [2, 1, 5, 6, 2, 3],
    [2, 4],
    [2, 1, 5, 5, 5, 3],
    [1, 1, 2, 3, 4, 4, 4, 4],
    [6, 2, 5, 4, 5, 1, 6]
]:
    print(str(nums) + '->' + str(main(nums)))
