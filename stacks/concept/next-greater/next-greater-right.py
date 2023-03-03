inputs = [
    [5, 3, 1, 2, 4],
    [1, 1, 2, 3, 4, 4]
]


# T=n,S=n
def main(nums):
    res = [-1] * len(nums)
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res


for nums in inputs:
    print(main(nums))

print()


# T=n,S=n
# res[i] = distance of next greater element on right of nums[i]
def main(nums):
    res = [-1] * len(nums)
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = i - stack[-1]
        stack.append(i)
    return res


for nums in inputs:
    print(main(nums))
