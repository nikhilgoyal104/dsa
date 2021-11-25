from heapq import *


# T=nlogn,S=n
def main(sticks):
    res = 0
    heapify(sticks)
    while len(sticks) > 1:
        cost = heappop(sticks) + heappop(sticks)
        res += cost
        heappush(sticks, cost)
    return res


for sticks in [
    [2, 4, 3],
    [1, 8, 3, 5],
    [5],
    [1, 2, 3, 4, 5]
]:
    print(main(sticks))
