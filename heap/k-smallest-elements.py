from heapq import *


# T=nlogk,S=k
def main(nums, k):
    heap = []
    for val in nums:
        heappush(heap, -val)
        if len(heap) > k:
            heappop(heap)
    while heap:
        print(-heappop(heap), end=' ')


for nums, k in [
    ([4, 7, 12, 6, 9, 8, 3, 1, 27, 19, 4, 31], 3)
]:
    main(nums, k)
