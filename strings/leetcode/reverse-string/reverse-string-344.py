# T=n,S=n
def x(s):
    def rec(low, high):
        if low < high:
            s[low], s[high] = s[high], s[low]
            rec(low + 1, high - 1)

    rec(0, len(s) - 1)


for s in [
    ['h', 'e', 'l', 'l', 'o'],
    ['h', 'a', 'n', 'n', 'a', 'h']
]:
    x(s)
    print(s)


# T=n,S=1
def y(s):
    low, high = 0, len(s) - 1
    while low < high:
        s[low], s[high] = s[high], s[low]
        low, high = low + 1, high - 1


for s in [
    ['h', 'e', 'l', 'l', 'o'],
    ['h', 'a', 'n', 'n', 'a', 'h']
]:
    y(s)
    print(s)
