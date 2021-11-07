from math import inf
from heapq import *


# T=k+nklogk,S=k
def main(arrays):
    heap = []
    start, end, maxVal = -inf, inf, -inf
    for i in range(len(arrays)):
        heap.append((arrays[i][0], i, 0, len(arrays[i])))
        maxVal = max(maxVal, arrays[i][0])
    heapify(heap)
    while heap:
        minVal, ri, ci, size = heappop(heap)
        if maxVal - minVal < end - start:
            start, end = minVal, maxVal
        if ci + 1 == size:
            return [start, end]
        heappush(heap, (arrays[ri][ci + 1], ri, ci + 1, size))
        maxVal = max(maxVal, arrays[ri][ci + 1])


for arrays in [
    [[1, 5, 8], [4, 12], [7, 8, 10]],
    [[1, 9], [4, 12], [7, 10, 16]]
]:
    print(main(arrays))
