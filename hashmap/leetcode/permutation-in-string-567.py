from collections import Counter


# T=m+26(n-m),S=1
def main(s1, s2):
    m, n = len(s1), len(s2)
    if m > n:
        return False
    s1Map, s2Map = Counter(s1), Counter(s2[:m])
    if s1Map == s2Map:
        return True
    for i in range(m, n):
        outgoing = s2[i - m]
        s2Map[outgoing] -= 1
        if not s2Map[outgoing]:
            del s2Map[outgoing]
        s2Map[s2[i]] += 1
        if s1Map == s2Map:
            return True
    return False


for s1, s2 in [
    ('ab', 'eidbaooo'),
    ('ab', 'eidboaoo'),
    ('ab', 'a')
]:
    print(main(s1, s2))
