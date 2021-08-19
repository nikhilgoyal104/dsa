from collections import Counter
from math import inf


def main(s):
    count, mfc = Counter(s), s[0]
    for ch in count:
        if count[ch] > count[mfc]:
            mfc = ch
    return mfc


for s in ['babcccdbabcccd']:
    print(main(s))
