# T=n,S=n
def main(nums):
    n = len(nums)
    stack, res = [], [-1] * n
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            res[stack.pop()] = nums[i % n]
        stack.append(i % n)
    return res


for nums in [
    [1, 2, 1], [1, 2, 3, 4, 3]
]:
    print(main(nums))
