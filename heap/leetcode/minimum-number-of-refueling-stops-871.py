from heapq import *

inputs = [
    (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]),
    (100, 1, [[10, 100]]),
    (1, 1, [])
]


# T=nlogn,S=n
def main(target, dist, stations):
    heap = []
    res = i = 0
    while dist < target:
        while i < len(stations) and stations[i][0] <= dist:
            heappush(heap, -stations[i][1])
            i += 1
        if not heap:
            return -1
        dist += -heappop(heap)
        res += 1
    return res


for target, startFuel, stations in inputs:
    print(main(target, startFuel, stations))
