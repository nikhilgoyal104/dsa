inputs = [
    'the sky is blue',
    '  hello world  ',
    'a good   example',
    '  Bob    Loves  Alice   '
]


# T=n,S=n
def main(s):
    return ' '.join(reversed(s.split()))


for s in inputs:
    print(main(s))

print()


def clean(s):
    n, res = len(s), []
    low, high = 0, len(s) - 1
    while low < n and s[low] == ' ':
        low += 1
    while high > -1 and s[high] == ' ':
        high -= 1
    while low <= high:
        if res and res[-1] == s[low] == ' ':
            pass
        else:
            res.append(s[low])
        low += 1
    return res


def reverse(s, low, high):
    while low < high:
        s[low], s[high] = s[high], s[low]
        low, high = low + 1, high - 1


# T=n,S=n
def main(s):
    s = clean(s)
    n, start = len(s), 0
    for end in range(n + 1):
        if end == n or s[end] == ' ':
            reverse(s, start, end - 1)
            start = end + 1
    reverse(s, 0, n - 1)
    return ''.join(s)


for s in inputs:
    print(main(s))
