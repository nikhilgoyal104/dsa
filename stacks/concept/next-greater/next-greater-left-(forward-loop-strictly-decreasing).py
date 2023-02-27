# (value)T=n²,S=1
def w(nums):
    res = []
    for i in range(len(nums)):
        nextGreater = -1
        for j in range(i - 1, -1, -1):
            if nums[j] > nums[i]:
                nextGreater = nums[j]
                break
        res.append(nextGreater)
    return res


# (value)T=n,S=n
def x(nums):
    res = []
    stack = []
    for val in nums:
        while stack and stack[-1] <= val:
            stack.pop()
        res.append(stack[-1] if stack else -1)
        stack.append(val)
    return res


# (index)T=n,S=n
def y(nums):
    res = []
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        res.append(stack[-1] if stack else -1)
        stack.append(i)
    return res


# (distance)T=n,S=n
def z(nums):
    res = []
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        res.append(i - stack[-1] if stack else -1)
        stack.append(i)
    return res


for nums in [
    [4, 5, 2, 25],
    [13, 7, 6, 12]
]:
    print(nums)
    print(w(nums))
    print(x(nums))
    print(y(nums))
    print(z(nums))
    print()
