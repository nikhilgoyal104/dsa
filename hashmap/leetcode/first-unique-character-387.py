from collections import Counter


# T=n²,S=1
def x(s):
    n = len(s)
    for i in range(n):
        isRepeated = False
        for j in range(n):
            if i != j and s[i] == s[j]:
                isRepeated = True
                break
        if not isRepeated:
            return i
    return -1


# T=n,S=1
def y(s):
    n = len(s)
    freq = Counter(s)
    for i in range(n):
        if freq[s[i]] == 1:
            return i
    return -1


# T=n,S=n
def z(s):
    res = float('inf')
    map = {}
    for i in range(len(s)):
        ch = s[i]
        if ch not in map:
            map[ch] = i
        else:
            map[ch] = -1
    for i in map.values():
        if i != -1:
            res = min(res, i)
    return -1 if res == float('inf') else res


for s in ['leetcode', 'loveleetcode', 'aabb']:
    print(x(s), end=' ')
    print(y(s), end=' ')
    print(z(s))
