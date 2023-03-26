from heapq import *

minHeap = []
maxHeap = []


def add(val):
    heappush(maxHeap, -val)
    heappush(minHeap, -heappop(maxHeap))
    if len(maxHeap) < len(minHeap):
        heappush(maxHeap, -heappop(minHeap))


def peek():
    if len(maxHeap) > len(minHeap):
        return -maxHeap[0]
    return (minHeap[0] + -maxHeap[0]) / 2


def main(nums):
    global minHeap, maxHeap
    minHeap = []
    maxHeap = []
    for val in nums:
        add(val)
        print(peek(), end=' ')


for nums in [
    [10, 20, 30, 40],
    [41, 35, 62, 5, 97, 108]
]:
    main(nums)
    print()
