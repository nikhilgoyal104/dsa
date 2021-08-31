from heapq import *
from collections import Counter


def x(words, k):
    freq = Counter(words)
    return nsmallest(k, freq.keys(), lambda x: (-freq[x], x))


# T=nlogk,S=n
def y(words, k):
    heap = []
    for word, f in Counter(words).items():
        heappush(heap, (f, word))
        if len(heap) > k:
            heappop(heap)
    return [word for _, word in heap]


for words, k in [
    (['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2),
]:
    print(x(words, k))
    print(y(words, k))
