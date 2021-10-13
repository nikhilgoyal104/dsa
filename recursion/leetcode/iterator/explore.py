from collections import deque

nums = deque([1, 2, 3])
print(nums)
nums.extend([8, 7, 6])
print(nums)

nums.extendleft([10, 54, 34])
print(nums)
