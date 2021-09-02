from collections import Counter


# T=n,S=n
def main(s):
    m, n = len(s), len(set(s))
    res, freq = m, Counter()
    right = left = 0
    while True:
        f1 = f2 = False
        while right < m and len(freq) < n:
            ch = s[right]
            freq[ch] += 1
            right += 1
            f1 = True
        while left < right and len(freq) == n:
            res = min(res, right - left)
            ch = s[left]
            freq[ch] -= 1
            if not freq[ch]:
                del freq[ch]
            left += 1
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
