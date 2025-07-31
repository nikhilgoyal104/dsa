from collections import Counter

inputs = [
    ('cbaebabacd', 'abc'),
    ('abab', 'ab')
]


# T=(m-n+1)n,S=(m-n+1)n
def main(s, p):
    m, n = len(s), len(p)
    res = []
    if n > m:
        return res
    freqP = Counter(p)
    for i in range(m - n + 1):
        freqS = Counter(s[i:i + n])
        if freqP == freqS:
            res.append(i)
    return res


for s, p in inputs:
    print(main(s, p))

print()


# T=n+(m-n),S=n
def main(s, p):
    m, n = len(s), len(p)
    res = []
    if n > m:
        return res
    freqP = Counter(p)
    freqS = Counter(s[:n])
    if freqP == freqS:
        res.append(0)
    for i in range(n, m):
        outgoing = s[i - n]
        incoming = s[i]
        freqS[outgoing] -= 1
        if not freqS[outgoing]:
            del freqS[outgoing]
        freqS[incoming] += 1
        if freqP == freqS:
            res.append(i - n + 1)
    return res


for s, p in inputs:
    print(main(s, p))
