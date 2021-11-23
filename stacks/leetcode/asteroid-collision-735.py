# T=n,S=n
def main(nums):
    i, n, stack = 0, len(nums), []
    while i < n:
        while stack and i < n and nums[i] < 0 < stack[-1]:
            if stack[-1] < abs(nums[i]):
                stack.pop()
            elif stack[-1] > abs(nums[i]):
                i += 1
            else:
                stack.pop()
                i += 1
        if i < n:
            stack.append(nums[i])
            i += 1
    return stack


for nums in [
    [-1, -2, 1, 3, 1, 2, -3, 3],
    [-2, 2, -1, -2],
    [-2, 1, -1, -2],
    [5, 10, -5],
    [10, 2, -5],
    [8, -8],
]:
    print(main(nums))
