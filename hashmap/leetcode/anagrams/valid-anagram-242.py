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
