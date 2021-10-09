from collections import Counter


# T=n,S=1
def main(s):
    res, vis = 0, set()
    freq = Counter(s)
    for count in freq.values():
        while count and count in vis:
            count -= 1
            res += 1
        vis.add(count)
    return res


for s in [
    'aab',
    'aaabbbcc',
    'ceabaacb'
]:
    print(main(s))
