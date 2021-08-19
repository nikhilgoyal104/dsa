from heapq import *


# T=nlogn,S=1
def u(nums, k):
    print(sorted(nums, reverse=True)[:k])


# T=nlogk,S=k
def v(nums, k):
    print(nlargest(k, nums))


# T=nlogk,S=k
def w(nums, k):
    heap = []
    for val in nums:
        heappush(heap, val)
        if len(heap) > k:
            heappop(heap)
    while heap:
        print(heappop(heap), end=' ')


# T=nlogk,S=k
def x(nums, k):
    n, heap = len(nums), []
    for i in range(n):
        if i < k:
            heappush(heap, nums[i])
        elif nums[i] > heap[0]:
            heappop(heap)
            heappush(heap, nums[i])
    while heap:
        print(heappop(heap), end=' ')


for nums, k in [
    ([11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45], 3),
    ([2, 10, 5, 17, 7, 18, 6, 4], 3)
]:
    u(nums, k)
    v(nums, k)
    w(nums, k)
    print()
    x(nums, k)
    print()
