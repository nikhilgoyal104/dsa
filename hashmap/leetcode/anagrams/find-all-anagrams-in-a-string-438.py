from collections import Counter


# T=n+26(m-n),S=1
def main(s, p):
    res, m, n = [], len(s), len(p)
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


for s, p in [
    ('cbaebabacd', 'abc'),
    ('abab', 'ab')
]:
    print(main(s, p))
