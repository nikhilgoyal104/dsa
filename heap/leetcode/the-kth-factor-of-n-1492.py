from math import sqrt
from heapq import heappush, heappop

inputs = [
    (12, 3),
    (7, 2),
    (4, 4),
    (1, 1),
    (1000, 3)
]


# T=n,S=1
def main(n, k):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            if count == k:
                return i
    return -1


for n, k in inputs:
    print(main(n, k), end=' ')

print()


# T=sqrt(n)logk,S=min(k,sqrt(n))
def main(n, k):
    heap = []

    def pushToHeap(num):
        heappush(heap, -num)
        if len(heap) > k:
            heappop(heap)

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            pushToHeap(i)
            if i != n // i:
                pushToHeap(n // i)

    return -heappop(heap) if k == len(heap) else -1


for n, k in inputs:
    print(main(n, k), end=' ')
