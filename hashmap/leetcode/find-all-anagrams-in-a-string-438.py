from collections import Counter


# T=n+26(m-n),S=1
def main(s, p):
    res, m, n = [], len(s), len(p)
    if n > m:
        return res
    sMap, pMap = Counter(s[:n]), Counter(p)
    if sMap == pMap:
        res.append(0)
    for i in range(n, m):
        outgoing = s[i - n]
        sMap[outgoing] -= 1
        if not sMap[outgoing]:
            del sMap[outgoing]
        sMap[s[i]] += 1
        if sMap == pMap:
            res.append(i - n + 1)
    return res


for s, p in [
    ('cbaebabacd', 'abc'),
    ('abab', 'ab')
]:
    print(main(s, p))
