from collections import Counter


# T=m+n,S=m+n
def main(s, t):
    m, n = len(s), len(t)
    res, sMap, tMap = '', Counter(), Counter(t)
    matchCount = i = j = 0
    while True:
        f1 = f2 = False
        while i < m and matchCount < n:
            ch = s[i]
            sMap[ch] += 1
            if sMap[ch] <= tMap[ch]:
                matchCount += 1
            i += 1
            f1 = True
        while j < i and matchCount == n:
            candidate = s[j:i]
            if not res or len(candidate) < len(res):
                res = candidate
            ch = s[j]
            sMap[ch] -= 1
            if sMap[ch] < tMap[ch]:
                matchCount -= 1
            j += 1
            f2 = True
        if not f1 and not f2:
            break
    return res


for s, t in [
    ('bbacacdcbbcaadcdca', 'abcd'),
    ('dbaecbbabdcaafbddcabgba', 'abbcdc'),
    ('ADOBECODEBANC', 'ABC'),
    ('geeksforgeeks', 'ork'),
    ('a', 'a'),
    ('a', 'aa')
]:
    print(main(s, t))
