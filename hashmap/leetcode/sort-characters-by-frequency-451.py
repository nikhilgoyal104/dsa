from collections import Counter


def w(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    nums = sorted(freq.items(), key=lambda x: -x[1])
    return ''.join((ch * f for ch, f in nums))


def x(s):
    freq = Counter(s)
    return ''.join(sorted(s, key=lambda x: (-freq[x], x)))


def y(s):
    return ''.join(ch * f for ch, f in Counter(s).most_common())


def z(s):
    count = Counter(s)
    buckets = [[] for _ in range(max(count.values()) + 1)]
    for ch, f in count.items():
        buckets[f].append(ch)
    res = []
    for i in range(len(buckets) - 1, 0, -1):
        for ch in buckets[i]:
            res.append(ch * i)
    return ''.join(res)


for s in ['tree', 'cccaaa', 'Aabb', 'loveleetcode']:
    print(w(s), end=' ')
    print(x(s), end=' ')
    print(y(s), end=' ')
    print(z(s), end=' ')
    print()
