from collections import Counter


# T=n,S=1
def main(s):
    res = 0
    vis = set()
    for count in Counter(s).values():
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
