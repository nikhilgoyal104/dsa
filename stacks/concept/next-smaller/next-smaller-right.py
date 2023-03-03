inputs = [
    [5, 3, 1, 2, 4],
    [1, 1, 2, 3, 4, 4]
]


# T=n,S=n
def main(nums):
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res


for nums in inputs:
    print(main(nums))

print()


# T=n,S=n
def main(nums):
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            res[stack.pop()] = i - stack[-1]
        stack.append(i)
    return res


for nums in inputs:
    print(main(nums))
