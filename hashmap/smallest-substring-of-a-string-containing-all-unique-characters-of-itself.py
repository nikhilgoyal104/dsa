from collections import Counter


# T=n,S=n
def main(s):
    m, n = len(s), len(set(s))
    res, freq = m, Counter()
    i = j = 0
    while True:
        f1 = f2 = False
        while i < m and len(freq) < n:
            freq[s[i]] += 1
            i += 1
            f1 = True
        while j < i and len(freq) == n:
            res = min(res, i - j)
            ch = s[j]
            freq[ch] -= 1
            if not freq[ch]:
                del freq[ch]
            j += 1
            f2 = True
        if not f1 and not f2:
            break
    return res


for s in [
    'bbacacdcbbcaadcdca',
    'aabcbcdbca',
    'aaab'
]:
    print(main(s))
