from collections import Counter


# T=n,S=1
def x(s):
    oddFrequencyCount = 0
    for count in Counter(s).values():
        oddFrequencyCount += count % 2
        if oddFrequencyCount > 1:
            return False
    return True


# T=n,S=1
def y(s):
    return sum(count % 2 for count in Counter(s).values() if count % 2) < 2


# T=n,S=1
def z(s):
    chars = set()
    for char in s:
        if char in chars:
            chars.remove(char)
        else:
            chars.add(char)
    return len(chars) in [0, 1]


for s in [
    'a',
    'aaa',
    'code',
    'aab',
    'civil',
    'carerac',
    'aabbccc'
]:
    print(x(s), end=' ')
    print(y(s), end=' ')
    print(z(s))
