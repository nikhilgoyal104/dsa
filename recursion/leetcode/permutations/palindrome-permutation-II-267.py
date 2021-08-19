from collections import Counter


def possible(s):
    oddFrequencyCount = 0
    for count in Counter(s).values():
        oddFrequencyCount += count % 2
        if oddFrequencyCount > 1:
            return False
    return True


# T=n!
def x(s):
    if not possible(s):
        return []
    items, vis = Counter(s).items(), set()
    mid, half = '', ''.join(char * (count // 2) for char, count in items)
    for char, count in items:
        if count % 2:
            mid = char
            break
    s, n = half, len(half)

    def dfs():
        if len(vis) == n:
            return ['']
        res = []
        for i in range(n):
            if i in vis or (i > 0 and i - 1 not in vis and s[i] == s[i - 1]):
                continue
            vis.add(i)
            for path in dfs():
                res.append(s[i] + path)
            vis.remove(i)
        return res

    return [perm + mid + perm[::-1] for perm in dfs()]


for s in [
    'madam',
    'malayalam',
    'aab',
    'abc',
    'aabb',
    'aabbccc',
    'aaaaaa',
    'ddddaaaa',
    'aabbhijkkjih'
]:
    print(x(s))
