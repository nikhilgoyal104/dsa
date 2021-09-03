from collections import Counter
from math import inf


# T=m+n,S=m+n
def main(s, t):
    m, n = len(s), len(t)
    sMap, tMap = Counter(), Counter(t)
    minLen = start = matched = i = j = 0
    while i < m:
        sMap[s[i]] += 1
        if sMap[s[i]] <= tMap[s[i]]:
            matched += 1
        while matched == n:
            if not minLen or i - j + 1 < minLen:
                start, minLen = j, i - j + 1
            sMap[s[j]] -= 1
            if sMap[s[j]] < tMap[s[j]]:
                matched -= 1
            j += 1
        i += 1
    return s[start:start + minLen]


for s, t in [
    ('bbacacdcbbcaadcdca', 'abcd'),
    ('dbaecbbabdcaafbddcabgba', 'abbcdc'),
    ('ADOBECODEBANC', 'ABC'),
    ('geeksforgeeks', 'ork'),
    ('a', 'a'),
    ('a', 'aa')
]:
    print(main(s, t))
