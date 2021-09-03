from collections import Counter


# T=n³,S=1
def x(s):
    res, n = 0, len(s)
    for i in range(n):
        for j in range(i, n):
            if j - i + 1 == len(set(s[i:j + 1])):
                res = max(res, j - i + 1)
    return res


# T=n²,S=1
def y(s):
    res, n = 0, len(s)
    for i in range(n):
        vis = set()
        for j in range(i, n):
            if s[j] in vis:
                break
            vis.add(s[j])
            if j - i + 1 == len(vis):
                res = max(res, j - i + 1)
    return res


# T=n,S=1
def z(s):
    n, freq = len(s), Counter()
    res = i = j = 0
    while i < n:
        freq[s[i]] += 1
        while freq[s[i]] > 1:
            freq[s[j]] -= 1
            j += 1
        res = max(res, i - j + 1)
        i += 1
    return res


for s in [
    'aaaaaa',
    'abbacbcdbadbdbbdcb',
    'abcddef',
    'abcabcbb',
    'bbbbb',
    'pwwkew',
    '',
    ' '
]:
    print(x(s), end=' ')
    print(y(s), end=' ')
    print(z(s))
