from collections import Counter
from heapq import *


# T=nlogk,S=k
def main(s):
    heap = [[-count, char] for char, count in Counter(s).items()]
    heapify(heap)
    res, prev = [], [0, '']
    while heap:
        curr = heappop(heap)
        res.append(curr[1])
        curr[0] += 1
        if prev[0] < 0:
            heappush(heap, prev)
        prev = curr
    return '' if len(res) != len(s) else ''.join(res)


for s in [
    'aab',
    'aaab',
    'abbabbaaab'
]:
    print(main(s))
