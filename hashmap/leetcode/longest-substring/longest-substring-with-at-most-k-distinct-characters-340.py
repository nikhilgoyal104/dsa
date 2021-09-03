from collections import Counter


# T=n,S=1
def main(s, k):
    freq, n = Counter(), len(s)
    res = i = j = 0
    while i < n:
        freq[s[i]] += 1
        while len(freq) > k:
            freq[s[j]] -= 1
            if not freq[s[j]]:
                del freq[s[j]]
            j += 1
        res = max(res, i - j + 1)
        i += 1
    return res


for s, k in [
    ('eceba', 2),
    ('aa', 1),
]:
    print(main(s, k))
