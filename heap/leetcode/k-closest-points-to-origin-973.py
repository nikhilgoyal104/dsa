from heapq import *


# T=nlogn
def x(points, k):
    return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:k]


# T=nlogk,S=k
def y(points, k):
    return nsmallest(k, points, key=lambda x: x[0] ** 2 + x[1] ** 2)


# T=nlogk,S=k
def z(points, k):
    heap = []
    for x, y in points:
        d = x ** 2 + y ** 2
        heappush(heap, (-d, [x, y]))
        if len(heap) > k:
            heappop(heap)
    return [point for _, point in heap]


for points, k in [
    ([[1, 3], [-2, 2]], 1),
    ([[3, 3], [5, -1], [-2, 4]], 2)
]:
    print(x(points, k))
    print(y(points, k))
    print(z(points, k))
