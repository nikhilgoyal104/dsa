from collections import Counter


# T=n,S=1
def main(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


for s, t in [
    ('anagram', 'nagaram'),
    ('rat', 'car')
]:
    print(main(s, t))
