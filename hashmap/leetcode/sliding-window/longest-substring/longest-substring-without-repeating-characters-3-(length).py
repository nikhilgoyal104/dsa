from collections import Counter

inputs = [
    'aaaaaa',
    'aabcbcdbca',
    'abbacbcdbadbdbbdcb',
    'abcddef',
    'abcabcbb',
    'bbbbb',
    'pwwkew',
    '',
    ' '
]


# T=n³,S=1
def main(s):
    res, n = 0, len(s)
    for i in range(n):
        for j in range(i, n):
            if j - i + 1 == len(set(s[i:j + 1])):
                res = max(res, j - i + 1)
    return res


for s in inputs:
    print(main(s), end=' ')

print()


# T=n²,S=1
def main(s):
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


for s in inputs:
    print(main(s), end=' ')

print()


# T=n,S=1
def main(s):
    res = left = 0
    freq = Counter()
    for right in range(len(s)):
        freq[s[right]] += 1
        while freq[s[right]] > 1:
            freq[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res


for s in inputs:
    print(main(s), end=' ')
