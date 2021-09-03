from collections import Counter


# T=n,S=n
def main(s):
    m, n = len(s), len(set(s))
    res, freq = m, Counter()
    i = j = 0
    while i < m:
        freq[s[i]] += 1
        while len(freq) == n:
            res = min(res, i - j + 1)
            freq[s[j]] -= 1
            if not freq[s[j]]:
                del freq[s[j]]
            j += 1
        i += 1
    return res


for s in [
    'bbacacdcbbcaadcdca',
    'aabcbcdbca',
    'aaab'
]:
    print(main(s))
