inputs = [
    ('abcdefg', 2),
    ('abcd', 2),
    ('a', 2),
    ('abcdefg', 3),
    ('abcdef', 8),
    ('hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl', 39)
]


def reverse(s, low, high):
    while low < high:
        s[low], s[high] = s[high], s[low]
        low, high = low + 1, high - 1


# T=n,S=n
def main(s, k):
    n = len(s)
    s = list(s)
    start = 0
    for i in range(n):
        if (i + 1) % (2 * k) == 0:
            reverse(s, start, start + k - 1)
            start = i + 1
    rem = n - start
    if rem < k:
        reverse(s, start, n - 1)
    elif k <= rem < 2 * k:
        reverse(s, start, start + k - 1)
    return ''.join(s)


for s, k in inputs:
    print(main(s, k), end=' ')

print()


# T=n,S=n
def main(s, k):
    s = list(s)
    for start in range(0, len(s), 2 * k):
        s[start:start + k] = reversed(s[start:start + k])
    return ''.join(s)


for s, k in inputs:
    print(main(s, k), end=' ')
