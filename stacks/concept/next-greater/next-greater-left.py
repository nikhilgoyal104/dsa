inputs = [
    [5, 3, 1, 2, 4],
    [1, 1, 2, 3, 4, 4]
]


# T=n,S=n
def main(nums):
    res = []
    stack = []
    for val in nums:
        while stack and stack[-1] <= val:
            stack.pop()
        res.append(stack[-1] if stack else -1)
        stack.append(val)
    return res


for nums in inputs:
    print(main(nums))

print()


# T=n,S=n
def main(nums):
    res = []
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        res.append(i - stack[-1] if stack else -1)
        stack.append(i)
    return res


for nums in inputs:
    print(main(nums))
