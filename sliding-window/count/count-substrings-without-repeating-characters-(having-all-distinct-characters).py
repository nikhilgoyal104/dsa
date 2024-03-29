from collections import Counter


# T=n³,S=1
def x(s):
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i, n):
            if j - i + 1 == len(set(s[i:j + 1])):
                res += 1
    return res


# T=n²,S=1
def y(s):
    n = len(s)
    res = 0
    for i in range(n):
        vis = set()
        for j in range(i, n):
            if s[j] in vis:
                break
            vis.add(s[j])
            if j - i + 1 == len(vis):
                res += 1
    return res


# T=n,S=1
def z(s):
    res = left = 0
    freq = Counter()
    for right in range(len(s)):
        freq[s[right]] += 1
        while freq[s[right]] > 1:
            freq[s[left]] -= 1
            left += 1
        res += (right - left + 1)
    return res


for s in [
    'aaaaaa',
    'aabcbcdbca',
    'abbacbcdbadbdbbdcb',
    'abcddef',
    'abcabcbb',
    'bbbbb',
    'pwwkew',
    'gffg',
    '',
    ' '
]:
    print(x(s), end=' ')
    print(y(s), end=' ')
    print(z(s))
