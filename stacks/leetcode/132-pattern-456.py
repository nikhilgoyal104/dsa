from math import inf


# T=n³,S=1
def x(nums):
    n = len(nums)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] < nums[k] < nums[j]:
                    return True
    return False


# T=n²,S=1
def y(nums):
    n = len(nums)
    minSoFar = [0] * n
    minSoFar[0] = nums[0]
    for i in range(1, n - 2):
        minSoFar[i] = min(minSoFar[i - 1], nums[i])
    for j in range(1, n - 1):
        for k in range(j + 1, n):
            if minSoFar[j - 1] < nums[k] < nums[j]:
                return True
    return False


# T=n,S=n
def z(nums):
    n = len(nums)
    if n < 3:
        return False
    stack, minSoFar = [], [0] * n
    minSoFar[0] = nums[0]
    for i in range(1, n - 2):
        minSoFar[i] = min(minSoFar[i - 1], nums[i])
    for j in range(n - 1, 0, -1):
        while stack and stack[-1] < nums[j]:
            if minSoFar[j - 1] < stack[-1]:
                return True
            stack.pop()
        stack.append(nums[j])
    return False


for nums in [
    [-2],
    [1, 2, 3, 4],
    [3, 1, 4, 2],
    [-1, 3, 2, 0],
    [3, 5, 0, 3, 4]
]:
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
