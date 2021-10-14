from collections import Counter
from math import inf


# T=m+n,S=m+n
def main(s, t):
    m, n = len(s), len(t)
    map1, map2 = Counter(), Counter(t)
    start = matched = left = 0
    minLen = inf
    for right in range(m):
        map1[s[right]] += 1
        if map1[s[right]] <= map2[s[right]]:
            matched += 1
        while matched == n:
            if right - left + 1 < minLen:
                start, minLen = left, right - left + 1
            map1[s[left]] -= 1
            if map1[s[left]] < map2[s[left]]:
                matched -= 1
            left += 1
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
