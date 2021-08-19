from heapq import *

nums = [9, 4, 5, 6, 1]
heapify(nums)
print(heappop(nums))
print(nlargest(3, nums))
print(nsmallest(3, nums))

nums = [9, 4, 5]
heapify(nums)
print(nums[0])
heappushpop(nums, 13)
print(nums[0], nums)

heap = []
for val in [9, 4, 5, 6, 1]:
    heappush(heap, -val)
while heap:
    print(-heappop(heap), end=' ')

print()

nums, b, c = [1, 2, 3], [5, 7, 9], [6, 8, 10]
print(list(merge(nums, b, c)))
