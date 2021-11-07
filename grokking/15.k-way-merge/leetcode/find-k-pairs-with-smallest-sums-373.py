from heapq import *


# T=mnlog(mn)
def x(nums1, nums2, k):
    pairs = [[first, second] for first in nums1 for second in nums2]
    pairs.sort(key=lambda x: x[0] + x[1])
    return pairs[:k]


# T=mnlogk,S=k
def y(nums1, nums2, k):
    heap = []
    for first in nums1:
        for second in nums2:
            heappush(heap, (-(first + second), [first, second]))
            if len(heap) > k:
                heappop(heap)
    return [pair for _, pair in heap]


# Let x=min(m,k)
# T=x+klogx,S=x
def z(nums1, nums2, k):
    res, heap = [], []
    for ri in range(min(len(nums1), k)):
        heap.append((nums1[ri] + nums2[0], [nums1[ri], nums2[0]], 0))
    heapify(heap)
    while k and heap:
        _, pair, ci = heappop(heap)
        res.append(pair)
        if ci + 1 < len(nums2):
            heappush(heap, (pair[0] + nums2[ci + 1], [pair[0], nums2[ci + 1]], ci + 1))
        k -= 1
    return res


for nums1, nums2, k in [
    ([1, 7, 11], [2, 4, 6], 3),
    ([1, 7, 11, 16], [2, 4, 6, 15], 3),
    ([1, 1, 2], [1, 2, 3], 2),
    ([1, 2], [3], 3),
    ([1, 2, 4, 5, 6], [3, 5, 7, 9], 3),
    ([1, 7, 11, 16], [2, 9, 10, 15], 2)
]:
    print(x(nums1, nums2, k))
    print(y(nums1, nums2, k))
    print(z(nums1, nums2, k))
