from collections import Counter

inputs = [
    ('anagram', 'nagaram'),
    ('rat', 'car')
]


# T=nlogn,S=n
def main(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


for s, t in inputs:
    print(main(s, t))


# T=n,S=1
def main(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


for s, t in inputs:
    print(main(s, t))


# T=n,S=1
def main(s, t):
    if len(s) != len(t):
        return False
    freq = Counter()
    for i in range(len(s)):
        freq[s[i]] += 1
        freq[t[i]] -= 1
    return not any(freq.values())


for s, t in inputs:
    print(main(s, t))


# T=n,S=1
def main(s, t):
    if len(s) != len(t):
        return False
    n = len(s)
    freq = Counter()
    for i in range(n):
        freq[s[i]] += 1
    for i in range(n):
        freq[t[i]] -= 1
        if freq[t[i]] < 0:
            return False
    return True


for s, t in inputs:
    print(main(s, t))
