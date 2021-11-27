from collections import Counter
from heapq import heappush, heappop

inputs = [
    ([5, 5, 4], 1),
    ([4, 3, 1, 1, 3, 3, 2], 3)
]


# T=nlogn,S=n
def main(nums, k):
    heap = []
    for count in Counter(nums).values():
        heappush(heap, count)
    while k:
        count = heappop(heap)
        if count > 1:
            heappush(heap, count - 1)
        k -= 1
    return len(heap)


for nums, k in inputs:
    print(main(nums, k))
