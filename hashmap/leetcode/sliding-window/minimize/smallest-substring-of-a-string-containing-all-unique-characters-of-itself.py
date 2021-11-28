from collections import Counter


# T=n,S=n
def main(s):
    n, unique = len(s), len(set(s))
    res, freq, left = n, Counter(), 0
    for right in range(n):
        freq[s[right]] += 1
        while len(freq) == unique:
            res = min(res, right - left + 1)
            freq[s[left]] -= 1
            if not freq[s[left]]:
                del freq[s[left]]
            left += 1
    return res


for s in [
    'bbacacdcbbcaadcdca',
    'aabcbcdbca',
    'aaab'
]:
    print(main(s))
