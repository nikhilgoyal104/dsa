# T=n,S=n
def main(s):
    def dfs(low, high):
        if low < high:
            s[low], s[high] = s[high], s[low]
            dfs(low + 1, high - 1)

    dfs(0, len(s) - 1)


for s in [
    ['h', 'e', 'l', 'l', 'o'],
    ['h', 'a', 'n', 'n', 'a', 'h']
]:
    main(s)
    print(s)

print()


# T=n,S=1
def main(s):
    low, high = 0, len(s) - 1
    while low < high:
        s[low], s[high] = s[high], s[low]
        low, high = low + 1, high - 1


for s in [
    ['h', 'e', 'l', 'l', 'o'],
    ['h', 'a', 'n', 'n', 'a', 'h']
]:
    main(s)
    print(s)
