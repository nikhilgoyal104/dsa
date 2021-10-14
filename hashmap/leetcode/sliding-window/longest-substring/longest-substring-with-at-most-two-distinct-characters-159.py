from collections import Counter


# T=n,S=1
def main(s):
    res, n = 0, len(s)
    freq, left = Counter(), 0
    for right in range(n):
        freq[s[right]] += 1
        while len(freq) > 2:
            freq[s[left]] -= 1
            if not freq[s[left]]:
                del freq[s[left]]
            left += 1
        res = max(res, right - left + 1)
    return res


for s in [
    'eceba',
    'ccaabbb'
]:
    print(main(s))
