from collections import Counter
from math import inf


# T=m+n,S=m+n
def main(s, t):
    m, n = len(s), len(t)
    map1, map2 = Counter(), Counter(t)
    start = matched = j = 0
    minLen = inf
    for i in range(m):
        map1[s[i]] += 1
        if map1[s[i]] <= map2[s[i]]:
            matched += 1
        while matched == n:
            if i - j + 1 < minLen:
                start, minLen = j, i - j + 1
            map1[s[j]] -= 1
            if map1[s[j]] < map2[s[j]]:
                matched -= 1
            j += 1
    return s[start:start + minLen if minLen != inf else 0]


for s, t in [
    ('bbacacdcbbcaadcdca', 'abcd'),
    ('dbaecbbabdcaafbddcabgba', 'abbcdc'),
    ('ADOBECODEBANC', 'ABC'),
    ('geeksforgeeks', 'ork'),
    ('a', 'a'),
    ('a', 'aa')
]:
    print(main(s, t))
