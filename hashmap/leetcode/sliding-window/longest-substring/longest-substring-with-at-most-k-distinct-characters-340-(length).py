from collections import Counter


# T=n,S=1
def main(s, k):
    res, n = 0, len(s)
    freq, left = Counter(), 0
    for right in range(n):
        freq[s[right]] += 1
        while len(freq) > k:
            char = s[left]
            freq[char] -= 1
            if not freq[char]:
                del freq[char]
            left += 1
        res = max(res, right - left + 1)
    return res


for s, k in [
    ('aaaaa', 3),
    ('aabacbebebe', 3),
    ('ddacbbaccdedacebb', 3),
    ('loveleetcode', 4),
    ('aaabc', 2),
    ('eceba', 2),
    ('aa', 1),
]:
    print(main(s, k))
