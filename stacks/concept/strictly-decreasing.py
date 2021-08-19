# T=n,S=n
def x(nums):
    n, stack = len(nums), []
    for i in range(n):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        stack.append(nums[i])
    return stack


# T=n,S=n
def y(nums):
    n, stack = len(nums), []
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        stack.append(i)
    return stack


for nums in [
    [7, 6, 6, 5, 5, 4, 3, 2, 1],
    [7, 6, 6, 5, 5, 4, 3, 8, 2, 1],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5]
]:
    print(x(nums), end=' ')
    print(y(nums))
