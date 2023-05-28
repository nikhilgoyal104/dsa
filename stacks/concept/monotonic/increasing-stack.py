inputs = [
    [7, 6, 6, 5, 5, 4, 3, 2, 1],
    [7, 6, 6, 5, 5, 4, 3, 8, 2, 1],
    [5, 4, 3, 2, 1],
    [5, 4, 1, 2, 3],
    [4, 5, 6, 1, 2],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 3, 5, 1]
]


# T=n,S=n
def main(nums):
    stack = []
    for val in nums:
        while stack and stack[-1] >= val:
            stack.pop()
        stack.append(val)
    return stack


for nums in inputs:
    print(main(nums))

print()


# T=n,S=n
def main(nums):
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        stack.append(i)
    return stack


for nums in inputs:
    print(main(nums))
