from math import inf
from heapq import *


# T=k+nklogk,S=k
def x(arrays):
    heap = []
    start, end, maximum = -inf, inf, -inf
    for i in range(len(arrays)):
        heap.append((arrays[i][0], i, 0, len(arrays[i])))
        maximum = max(maximum, arrays[i][0])
    heapify(heap)
    while heap:
        minimum, ri, ci, size = heappop(heap)
        if maximum - minimum < end - start:
            start, end = minimum, maximum
        if ci + 1 == size:
            return [start, end]
        heappush(heap, (arrays[ri][ci + 1], ri, ci + 1, size))
        maximum = max(maximum, arrays[ri][ci + 1])


for arrays in [
    [[1, 5, 8], [4, 12], [7, 8, 10]],
    [[1, 9], [4, 12], [7, 10, 16]]
]:
    print(x(arrays))
