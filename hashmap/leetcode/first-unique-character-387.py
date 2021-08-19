from collections import Counter, defaultdict
from math import inf


def x(s):
    frequency = Counter(s)
    for i, ch in enumerate(s):
        if frequency[ch] == 1:
            return i
    return -1


def y(s):
    map = {}
    for i, ch in enumerate(s):
        if ch not in map:
            map[ch] = (0, i)
        map[ch] = (map[ch][0] + 1, map[ch][1])
    res = inf
    for _, (count, firstOccurenceIndex) in map.items():
        if count == 1:
            res = min(res, firstOccurenceIndex)
    return -1 if res == inf else res


def bf(s):
    n = len(s)
    for i in range(n):
        repeated = False
        for j in range(n):
            if i != j and s[i] == s[j]:
                repeated = True
                break
        if not repeated:
            return i
    return -1


for s in ['leetcode', 'loveleetcode', 'aabb']:
    print(bf(s), end=' ')
    print(x(s), end=' ')
    print(y(s), end=' ')
    print()
