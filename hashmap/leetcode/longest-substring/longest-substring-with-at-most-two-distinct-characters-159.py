from collections import Counter


# T=n,S=1
def main(s):
    n, freq = len(s), Counter()
    res = i = j = 0
    while i < n:
        freq[s[i]] += 1
        while len(freq) > 2:
            freq[s[j]] -= 1
            if not freq[s[j]]:
                del freq[s[j]]
            j += 1
        res = max(res, i - j + 1)
        i += 1
    return res


for s in [
    'eceba',
    'ccaabbb'
]:
    print(main(s))
