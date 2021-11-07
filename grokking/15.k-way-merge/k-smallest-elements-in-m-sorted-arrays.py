from heapq import *


# T=m+klogm,S=m+k
def main(arrays, k):
    res, heap = [], []
    for i in range(len(arrays)):
        if arrays[i]:
            heap.append((arrays[i][0], i, 0, len(arrays[i])))
    heapify(heap)
    for _ in range(k):
        val, ri, ci, size = heappop(heap)
        res.append(val)
        if ci + 1 < size:
            heappush(heap, (arrays[ri][ci + 1], ri, ci + 1, size))
    return res


for arrays, k in [
    ([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5),
    ([[5, 8, 9], [1, 7]], 3),
]:
    print(main(arrays, k))
