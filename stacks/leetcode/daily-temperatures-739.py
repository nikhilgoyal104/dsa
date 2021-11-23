# T=n,S=n
def main(nums):
    n = len(nums)
    stack, res = [], [0] * n
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            pos = stack.pop()
            res[pos] = i - pos
        stack.append(i)
    return res


for nums in [
    [73, 74, 75, 71, 69, 72, 76, 73],
    [30, 40, 50, 60],
    [30, 60, 90]
]:
    print(main(nums))
