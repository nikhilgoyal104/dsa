# T=n,S=n
def main(s):
    n, s = len(s), list(s)
    low, high = 0, n - 1
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    while low < high:
        while low < high and s[low] not in vowels:
            low += 1
        while low < high and s[high] not in vowels:
            high -= 1
        s[low], s[high] = s[high], s[low]
        low, high = low + 1, high - 1
    return ''.join(s)


for s in [
    'xyz', 'hello', 'leetcode', 'aA', 'a.b,.', '.,'
]:
    print(main(s))
