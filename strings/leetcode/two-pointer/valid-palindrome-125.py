inputs = [
    'A man, a plan, a canal: Panama',
    'race a car',
    '0P'
]


# T=n,S=n
def main(s):
    s = ''.join(ch for ch in s.lower() if ch.isalnum())
    low, high = 0, len(s) - 1
    while low < high:
        if s[low] != s[high]:
            return False
        low, high = low + 1, high - 1
    return True


for s in inputs:
    print(main(s), end=' ')

print()


# T=n,S=n
def main(s):
    s = ''.join(ch for ch in s.lower() if ch.isalnum())
    return s == s[::-1]


for s in inputs:
    print(main(s), end=' ')

print()


# T=n,S=1
def main(s):
    low, high = 0, len(s) - 1
    while low < high:
        while low < high and not s[low].isalnum():
            low += 1
        while low < high and not s[high].isalnum():
            high -= 1
        if s[low].lower() != s[high].lower():
            return False
        low, high = low + 1, high - 1
    return True


for s in inputs:
    print(main(s), end=' ')
