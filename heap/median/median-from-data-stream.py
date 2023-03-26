from heapq import *

minHeap = []
maxHeap = []


def add(val):
    if maxHeap and val > maxHeap[0]:
        heappush(maxHeap, val)
    else:
        heappush(minHeap, -val)
    balance()


def balance():
    n1, n2 = len(minHeap), len(maxHeap)
    if n1 - n2 == 2:
        heappush(maxHeap, -heappop(minHeap))
    elif n2 - n1 == 2:
        heappush(minHeap, -heappop(maxHeap))


def peek():
    n1, n2 = len(minHeap), len(maxHeap)
    if n1 + n2 == 0:
        return
    if n1 == n2:
        return (-minHeap[0] + maxHeap[0]) / 2
    elif n1 - n2 == 1:
        return -minHeap[0]
    elif n2 - n1 == 1:
        return maxHeap[0]


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
