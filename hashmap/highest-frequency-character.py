from collections import Counter


def main(s):
    count, res = Counter(s), s[0]
    for ch in count:
        if count[ch] > count[res]:
            res = ch
    return res


for s in ['babcccdbabcccd']:
    print(main(s))
