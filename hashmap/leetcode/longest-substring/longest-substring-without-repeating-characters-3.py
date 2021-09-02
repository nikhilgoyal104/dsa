from collections import Counter


def main(s):
    n, freq = len(s), Counter()
    res = i = j = 0
    while True:
        f1 = f2 = False
        while i < n:
            ch = s[i]
            freq[ch] += 1
            if freq[ch] > 1:
                res = max(res, i - j)
                i += 1
                break
            i += 1
            f1 = True
        while j < i:
            ch = s[j]
            freq[ch] -= 1
            if freq[ch] == 1:
                j += 1
                break
            j += 1
            f2 = True
        if not f1 and not f2:
            break
    return res


for s in [
    'abbacbcdbadbdbbdcb',
    'abcabcbb',
    'bbbbb',
    'pwwkew'
]:
    print(main(s))
