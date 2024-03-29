# T=n,S=n
def main(nums):
    n = len(nums)
    res = [0] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = i - stack[-1]
        stack.append(i)
    return res


for nums in [
    [73, 74, 75, 71, 69, 72, 76, 73],
    [30, 40, 50, 60],
    [30, 60, 90]
]:
    print(main(nums))
