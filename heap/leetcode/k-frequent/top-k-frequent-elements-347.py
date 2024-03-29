from heapq import *
from collections import Counter


# T=nlogn,S=n
def x(nums, k):
    freq = Counter(nums)
    return sorted(freq.keys(), key=freq.get, reverse=True)[:k]


# T=nlogk,S=k
def y(nums, k):
    freq = Counter(nums)
    return nlargest(k, freq.keys(), key=freq.get)


# T=nlogk,S=n+k
def z(nums, k):
    heap = []
    for val, count in Counter(nums).items():
        heappush(heap, (count, val))
        if len(heap) > k:
            heappop(heap)
    while heap:
        res.append(heappop(heap)[1])
    return res


for nums, k in [
    ([1, 1, 1, 2, 2, 3], 2),
    ([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], 4)
]:
    print(x(nums, k))
    print(y(nums, k))
    print(z(nums, k))
