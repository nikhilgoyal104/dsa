from collections import Counter
from math import inf


# T=n²,S=1
def x(s):
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


# T=n,S=1
def y(s):
    freq = Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1


# T=n,S=n
def z(s):
    res, map = inf, {}
    for i, ch in enumerate(s):
        map[ch] = i if ch not in map else -1
    for index in map.values():
        if index != -1:
            res = min(res, index)
    return -1 if res == inf else res


for s in ['leetcode', 'loveleetcode', 'aabb']:
    print(x(s), end=' ')
    print(y(s), end=' ')
    print(z(s))
