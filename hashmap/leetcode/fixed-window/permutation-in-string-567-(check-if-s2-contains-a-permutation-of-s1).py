from collections import Counter

inputs = [
    ('ab', 'eidbaooo'),
    ('ab', 'xyzabpqrbamno'),
    ('ab', 'a')
]


# T=(n-m+1)m,S=(n-m+1)m
def main(s1, s2):
    m, n = len(s1), len(s2)
    if m > n:
        return False
    freq1 = Counter(s1)
    for i in range(n - m + 1):
        freq2 = Counter(s2[i:i + m])
        if freq1 == freq2:
            return True
    return False


for s1, s2 in inputs:
    print(main(s1, s2))

print()


# T=m+(n-m),S=1
def main(s1, s2):
    m, n = len(s1), len(s2)
    if m > n:
        return False
    freq1 = Counter(s1)
    freq2 = Counter(s2[:m])
    if freq1 == freq2:
        return True
    for i in range(m, n):
        outgoing = s2[i - m]
        incoming = s2[i]
        freq2[outgoing] -= 1
        if not freq2[outgoing]:
            del freq2[outgoing]
        freq2[incoming] += 1
        if freq1 == freq2:
            return True
    return False


for s1, s2 in inputs:
    print(main(s1, s2))
