# (value)T=n,S=n
def x(nums):
    stack = []
    for val in nums:
        while stack and stack[-1] < val:
            stack.pop()
        stack.append(val)
    return stack


# (index)T=n,S=n
def y(nums):
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            stack.pop()
        stack.append(i)
    return stack


for nums in [
    [7, 6, 6, 5, 5, 4, 3, 2, 1],
    [7, 6, 6, 5, 5, 4, 3, 8, 2, 1],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5]
]:
    print(nums)
    print(x(nums))
    print(y(nums))
    print()
