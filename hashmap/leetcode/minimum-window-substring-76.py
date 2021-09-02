from collections import Counter


# T=m+n,S=m+n
def main(s, t):
    m, n = len(s), len(t)
    res, sMap, tMap = '', Counter(), Counter(t)
    matchCount = right = left = 0
    while True:
        f1 = f2 = False
        while right < m and matchCount < n:
            ch = s[right]
            sMap[ch] += 1
            if sMap[ch] <= tMap[ch]:
                matchCount += 1
            right += 1
            f1 = True
        while left < right and matchCount == n:
            candidate = s[left:right]
            if not res or len(candidate) < len(res):
                res = candidate
            ch = s[left]
            sMap[ch] -= 1
            if not sMap[ch]:
                del sMap[ch]
            if sMap[ch] < tMap[ch]:
                matchCount -= 1
            left += 1
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
