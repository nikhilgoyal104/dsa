from heapq import *


# T=nlogk+mlogk,S=k
class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for val in nums:
            self.add(val)

    def add(self, val):
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]


kthLargst = KthLargest(3, [4, 5, 8, 2])
print(kthLargst.add(3))
print(kthLargst.add(5))
print(kthLargst.add(10))
print(kthLargst.add(9))
print(kthLargst.add(4))
