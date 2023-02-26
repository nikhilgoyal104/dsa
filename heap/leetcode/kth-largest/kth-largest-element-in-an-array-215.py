from heapq import *


# T=nlogn
def x(nums, k):
    return sorted(nums)[-k]


# T=nlogk,S=k
def y(nums, k):
    heap = []
    for val in nums:
        heappush(heap, val)
        if len(heap) > k:
            heappop(heap)
    return heappop(heap)


# T=nlogk,S=k
def z(nums, k):
    return nlargest(k, nums)[-1]


for nums, k in [
    ([3, 2, 1, 5, 6, 4], 2),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
]:
    print(x(nums, k), end=' ')
    print(y(nums, k), end=' ')
    print(z(nums, k))
