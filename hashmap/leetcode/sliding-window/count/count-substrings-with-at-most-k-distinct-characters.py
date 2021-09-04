from collections import Counter


# T=n,S=1
def main(s, k):
    res, n = 0, len(s)
    freq, j = Counter(), 0
    for i in range(n):
        freq[s[i]] += 1
        while len(freq) > k:
            freq[s[j]] -= 1
            if not freq[s[j]]:
                del freq[s[j]]
            j += 1
        res += (i - j + 1)
    return res


for s, k in [
    ('aaaaa', 3),
    ('aabcbcdbca', 2),
    ('aabacbebebe', 3),
    ('ddacbbaccdedacebb', 3),
    ('loveleetcode', 4),
    ('aaabc', 2),
    ('eceba', 2),
    ('aa', 1),
]:
    print(main(s, k))
