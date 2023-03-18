inputs = [
    '110001111000000',
    '00110011',
    '10101'
]


# T=n,S=n
def main(s):
    groups = [1]
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            groups.append(1)
            continue
        groups[-1] += 1
    res = 0
    for i in range(1, len(groups)):
        res += min(groups[i - 1], groups[i])
    return res


for s in inputs:
    print(main(s), end=' ')

print()


# T=n,S=1
def main(s):
    res = previous = 0
    current = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            res += min(previous, current)
            previous = current
            current = 1
            continue
        current += 1
    return res + min(previous, current)


for s in inputs:
    print(main(s), end=' ')
