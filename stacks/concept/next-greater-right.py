# T=n²,S=1
def w(nums):
    n = len(nums)
    res = [None] * n
    for i in range(n):
        nge = -1
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                nge = nums[j]
                break
        res[i] = nge
    return res


# T=n,S=n
def x(nums):
    n = len(nums)
    stack, res = [], [None] * n
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    return res


# T=n,S=n
def y(nums):
    n = len(nums)
    stack, res = [], [None] * n
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(i)
    return res


# T=n,S=n
def z(nums):
    n = len(nums)
    stack, res = [], [None] * n
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        res[i] = stack[-1] - i if stack else -1
        stack.append(i)
    return res


for nums in [
    [4, 5, 2, 25],
    [13, 7, 6, 12],
    [2, 5, 9, 3, 1, 12, 6, 8, 7]
]:
    print(w(nums), end=' ')
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
