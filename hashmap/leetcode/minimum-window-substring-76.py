from collections import Counter


def main(s, t):
    m, n = len(s), len(t)
    tMap, sMap = Counter(t), Counter()
    matchCount = i = 0
    while i < m:
        sMap[s[i]] += 1
        if sMap[s[i]] <= tMap[s[i]]:
            matchCount += 1
        if matchCount == n:
            break
        i += 1
    j = 0
    while j < m:
        j += 1


for s, t in [
    ('ADOBECODEBANC', 'ABC'),
    ('a', 'a'),
    ('a', 'aa')
]:
    print(main(s, t))
