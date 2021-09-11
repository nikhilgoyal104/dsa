# T=n,S=n
def x(s):
    s = ''.join(ch for ch in s.lower() if ch.isalnum())
    low, high = 0, len(s) - 1
    while low < high:
        if s[low] != s[high]:
            return False
        low, high = low + 1, high - 1
    return True


# T=n,S=n
def y(s):
    s = ''.join(ch for ch in s.lower() if ch.isalnum())
    return s == s[::-1]


# T=n,S=1
def z(s):
    pass


for s in [
    'A man, a plan, a canal: Panama',
    'race a car',
    '0P'
]:
    print(x(s), end=' ')
    print(y(s))
