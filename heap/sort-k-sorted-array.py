from heapq import *


def main(nums, k):
    heap, n = [], len(nums)
    for i in range(n):
        if i < k + 1:
            heappush(heap, nums[i])
        else:
            print(heappop(heap), end=' ')
            heappush(heap, nums[i])
    while heap:
        print(heappop(heap), end=' ')


for nums, k in [
    ([2, 3, 1, 4, 6, 7, 5, 8, 9], 2),
    ([6, 5, 3, 2, 8, 10, 9], 3),
    ([10, 9, 8, 7, 4, 70, 60, 50], 4),
    ([1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2)
]:
    main(nums, k)
    print()
