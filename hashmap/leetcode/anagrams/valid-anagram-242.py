from collections import Counter


# T=n,S=1
def main(s, t):
    return Counter(s) == Counter(t)


for s, t in [
    ('anagram', 'nagaram'),
    ('rat', 'car')
]:
    print(main(s, t))
