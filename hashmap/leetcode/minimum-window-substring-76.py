from collections import Counter


def main(s, t):
    m, n = len(s), len(t)
    res, sMap, tMap = '', Counter(), Counter(t)
    matchCount = i = j = 0
    while True:
        f1 = f2 = False
        while i < m and matchCount < n:
            sMap[s[i]] += 1
            if sMap[s[i]] <= tMap[s[i]]:
                matchCount += 1
            i += 1
            f1 = True
        while j < i and matchCount == n:
            candidate = s[j:i]
            if not res or len(candidate) < len(res):
                res = candidate
            sMap[s[j]] -= 1
            if not sMap[s[j]]:
                del sMap[s[j]]
            if sMap[s[j]] < tMap[s[j]]:
                matchCount -= 1
            j += 1
            f2 = True
        if not f1 and not f2:
            break
    return res


for s, t in [
    ('dbaecbbabdcaafbddcabgba', 'abbcdc'),
    ('ADOBECODEBANC', 'ABC'),
    ('a', 'a'),
    ('a', 'aa')
]:
    print(main(s, t))
