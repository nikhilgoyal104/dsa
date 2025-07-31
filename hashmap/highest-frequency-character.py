from collections import Counter


def main(s):
    res = s[0]
    freq = Counter(s)
    for ch in freq:
        if freq[ch] > freq[res]:
            res = ch
    return res


for s in ['babcccdbabcccd']:
    print(main(s))
