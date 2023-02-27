# (right value)T=n,S=n
def x(nums):
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res


# (right distance)T=n,S=n
def y(nums):
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = i - stack[-1]
        stack.append(i)
    return res


for nums in [
    [5, 3, 1, 2, 4],
    [1, 1, 2, 3, 4, 4]
]:
    print(nums)
    print(x(nums))
    print(y(nums))
    print()


# (left value)T=n,S=n
def x(nums):
    res = []
    stack = []
    for val in nums:
        while stack and stack[-1] <= val:
            stack.pop()
        res.append(stack[-1] if stack else -1)
        stack.append(val)
    return res


# (left distance)T=n,S=n
def y(nums):
    res = []
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        res.append(i - stack[-1] if stack else -1)
        stack.append(i)
    return res


for nums in [
    [5, 3, 1, 2, 4],
    [1, 1, 2, 3, 4, 4]
]:
    print(nums)
    print(x(nums))
    print(y(nums))
    print()
