from collections import Counter


# T=n,S=1
def main(s):
    res, n = 0, len(s)
    freq, j = Counter(), 0
    for i in range(n):
        freq[s[i]] += 1
        while len(freq) > 2:
            freq[s[j]] -= 1
            if not freq[s[j]]:
                del freq[s[j]]
            j += 1
        res = max(res, i - j + 1)
    return res


for s in [
    'eceba',
    'ccaabbb'
]:
    print(main(s))
