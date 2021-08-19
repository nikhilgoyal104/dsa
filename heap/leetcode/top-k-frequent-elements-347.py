from heapq import *
from collections import Counter


# T=nlogn,S=1
def x(nums, k):
    frequency = Counter(nums)
    return sorted(frequency.keys(), key=frequency.get, reverse=True)[:k]


# T=nlogk,S=k
def y(nums, k):
    frequency = Counter(nums)
    return nlargest(k, frequency.keys(), key=frequency.get)


# T=nlogk,S=k
def z(nums, k):
    heap = []
    for val, f in Counter(nums).items():
        heappush(heap, (f, val))
        if len(heap) > k:
            heappop(heap)
    return [val for _, val in heap]


for nums, k in [
    ([1, 1, 1, 2, 2, 3], 2),
    ([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], 4)
]:
    print(x(nums, k))
    print(y(nums, k))
    print(z(nums, k))
