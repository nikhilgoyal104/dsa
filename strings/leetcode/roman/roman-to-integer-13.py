inputs = [
    'III', 'IV', 'IX', 'LVIII', 'MCMXCIV', 'MMMCMXCIX'
]


# T=1,S=1
def main(s):
    map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = i = 0
    n = len(s)
    while i < n:
        if i < n - 1 and map[s[i]] < map[s[i + 1]]:
            res += (map[s[i + 1]] - map[s[i]])
            i += 2
        else:
            res += map[s[i]]
            i += 1
    return res


for s in inputs:
    print(main(s), end=' ')

print()


# T=1,S=1
def main(s):
    map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
        'CD': 400, 'CM': 900
    }
    res = i = 0
    n = len(s)
    while i < n:
        if i < n - 1 and s[i:i + 2] in map:
            res += map[s[i:i + 2]]
            i += 2
        else:
            res += map[s[i]]
            i += 1
    return res


for s in inputs:
    print(main(s), end=' ')
