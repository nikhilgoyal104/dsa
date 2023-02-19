from collections import Counter

inputs = [
    ('cbaebabacd', 'abc'),
    ('abab', 'ab')
]


def anagram(p, substring):
    return Counter(p) == Counter(substring)


# T=(m-n+1)n,S=(m-n+1)n
def main(s, p):
    m, n = len(s), len(p)
    res = []
    if n > m:
        return res
    for i in range(m - n + 1):
        if anagram(p, s[i:i + n]):
            res.append(i)
    return res


for s, p in inputs:
    print(main(s, p))

print()


# T=n+(m-n),S=1
def main(s, p):
    m, n = len(s), len(p)
    res = []
    if n > m:
        return res
    map1, map2 = Counter(s[:n]), Counter(p)
    if map1 == map2:
        res.append(0)
    for i in range(n, m):
        map1[s[i - n]] -= 1
        if not map1[s[i - n]]:
            del map1[s[i - n]]
        map1[s[i]] += 1
        if map1 == map2:
            res.append(i - n + 1)
    return res


for s, p in inputs:
    print(main(s, p))
