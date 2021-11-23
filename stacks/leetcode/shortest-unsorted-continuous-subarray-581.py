inputs = [
    [2, 6, 4, 8, 10, 9, 15],
    [1, 2, 3, 4],
    [2, 1],
    [1]
]


# T=n²,S=1
def main(nums):
    n = len(nums)
    left, right = n - 1, 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                left, right = min(left, i), max(right, j)
    return 0 if (left == n - 1 and right == 0) else right - left + 1


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=nlogn,S=n
def main(nums):
    n, sortedNums = len(nums), sorted(nums)
    left, right = 0, 0
    for i in range(n):
        if nums[i] != sortedNums[i]:
            left = i
            break
    for i in range(n - 1, -1, -1):
        if nums[i] != sortedNums[i]:
            right = i
            break
    return 0 if left is right else right - left + 1


for nums in inputs:
    print(main(nums), end=' ')

print()


# T=n,S=n
def main(nums):
    n = len(nums)
    left, stack = n - 1, []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            left = min(left, stack.pop())
        stack.append(i)
    right, stack = 0, []
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] < nums[i]:
            right = max(right, stack.pop())
        stack.append(i)
    return 0 if (left == n - 1 and right == 0) else right - left + 1


for nums in inputs:
    print(main(nums), end=' ')
