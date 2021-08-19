import bisect

nums = [1, 2, 3, 3, 4, 4, 5]

print(bisect.bisect(nums, 4))
print(bisect.bisect(nums, 5))
print(bisect.bisect(nums, 6))

print()
print(bisect.bisect_right(nums, 4))
print(bisect.bisect_right(nums, 5))
print(bisect.bisect_right(nums, 6))

print()
print(bisect.bisect_left(nums, 4))
print(bisect.bisect_left(nums, 5))
print(bisect.bisect_left(nums, 6))
