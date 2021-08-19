from heapq import *


def main(lst):
    heap, n = [], len(lst)
    for val in lst:
        heappush(heap, val)
    for _ in range(n):
        print(heappop(heap), end=' ')


for lst in [
    [10, 2, 80, 9, 33],
    [17, 33, 27, 14, 18, 19, 21, 11, 9, 5],
    [8, 3, 6, 5, 9, 1]
]:
    main(lst)
    print()
