# T=n,S=n
def x(nums):
    n = len(nums)
    stack, res = [], [-1] * n
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res


# T=n,S=n
def y(nums):
    n = len(nums)
    stack, res = [], [-1] * n
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            pos = stack.pop()
            res[pos] = i - pos
        stack.append(i)
    return res


for nums in [
    [5, 3, 1, 2, 4],
    [1, 1, 2, 3, 4, 4]
]:
    print(x(nums))
    print(y(nums))

print()


# T=n,S=n
def x(nums):
    n = len(nums)
    stack, res = [], [-1] * n
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        res[i] = nums[stack[-1]] if stack else -1
        stack.append(i)
    return res


# T=n,S=n
def y(nums):
    n = len(nums)
    stack, res = [], [-1] * n
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        res[i] = i - stack[-1] if stack else -1
        stack.append(i)
    return res


for nums in [
    [5, 3, 1, 2, 4],
    [1, 1, 2, 3, 4, 4]
]:
    print(x(nums))
    print(y(nums))
