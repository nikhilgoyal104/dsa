def reverse(s, low, high):
    while low < high:
        s[low], s[high] = s[high], s[low]
        low, high = low + 1, high - 1


# T=n,S=1
def main(s):
    n, start = len(s), 0
    for end in range(n + 1):
        if end == n or s[end] == ' ':
            reverse(s, start, end - 1)
            start = end + 1
    reverse(s, 0, n - 1)


for s in [
    ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e'],
    ['a']
]:
    main(s)
    print(s)
