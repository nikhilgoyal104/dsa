from heapq import *

inputs = [
    ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8),
    ([[-5]], 1),
    ([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5),
    ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 2)
]


# T=n²logk,S=k
def main(grid, k):
    heap = []
    for row in grid:
        for val in row:
            heappush(heap, -val)
            if len(heap) > k:
                heappop(heap)
    return -heappop(heap)


for grid, k in inputs:
    print(main(grid, k), end=' ')

print()


# Let x=min(k,n)
# T=x+klogx,S=x
def main(grid, k):
    res, n = None, len(grid)
    heap = [(grid[ri][0], ri, 0) for ri in range(min(k, n))]
    heapify(heap)
    for _ in range(k):
        res, ri, ci = heappop(heap)
        if ci + 1 < n:
            heappush(heap, (grid[ri][ci + 1], ri, ci + 1))
    return res


# 1<=k<=n²
for grid, k in inputs:
    print(main(grid, k), end=' ')
