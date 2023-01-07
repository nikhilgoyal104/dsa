# T=n,S=n
def x(s):
    return ' '.join(word[::-1] for word in s.split())


def reverse(s, low, high):
    while low < high:
        s[low], s[high] = s[high], s[low]
        low, high = low + 1, high - 1


# T=n,S=n
def y(s):
    n = len(s)
    s = list(s)
    start = 0
    for end in range(n):
        if s[end] == ' ':
            reverse(s, start, end - 1)
            start = end + 1
    reverse(s, start, n - 1)
    return ''.join(s)


# T=n,S=n
def z(s):
    n = len(s)
    s = list(s)
    start = 0
    for end in range(n + 1):
        if end == n or s[end] == ' ':
            reverse(s, start, end - 1)
            start = end + 1
    return ''.join(s)


for s in [
    "Let's take LeetCode contest", "God Ding"
]:
    print(x(s), end=' ')
    print(y(s), end=' ')
    print(z(s))
