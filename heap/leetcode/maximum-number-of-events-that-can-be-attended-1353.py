from heapq import heappush, heappop


# T=nlogn,S=n
def main(events):
    n = len(events)
    events = sorted(events)
    i = res = day = 0
    heap = []
    while i < n or heap:
        if not heap:
            day = events[i][0]
        while i < n and day == events[i][0]:
            heappush(heap, events[i][1])
            i += 1
        heappop(heap)
        res += 1
        day += 1
        while heap and day > heap[0]:
            heappop(heap)
    return res


for events in [
    [[1, 2], [2, 3], [3, 4]],
    [[1, 2], [2, 3], [3, 4], [1, 2]],
    [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]],
    [[1, 100000]],
    [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]
]:
    print(main(events))
