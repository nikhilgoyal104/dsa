from collections import Counter


# T=m+26(n-m),S=1
def main(s1, s2):
    m, n = len(s1), len(s2)
    if m > n:
        return False
    map1, map2 = Counter(s1), Counter(s2[:m])
    if map1 == map2:
        return True
    for i in range(m, n):
        map2[s2[i - m]] -= 1
        if not map2[s2[i - m]]:
            del map2[s2[i - m]]
        map2[s2[i]] += 1
        if map1 == map2:
            return True
    return False


for s1, s2 in [
    ('ab', 'eidbaooo'),
    ('ab', 'eidboaoo'),
    ('ab', 'a')
]:
    print(main(s1, s2))
