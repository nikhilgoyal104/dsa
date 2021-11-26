from collections import Counter, defaultdict

inputs = [
    'ABC',
    'ABA',
    'LEETCODE',
    'LETTER'
]


# T=n³,S=n
def main(s):
    res, n = 0, len(s)
    for i in range(n):
        for j in range(i, n):
            freq = Counter(s[i:j + 1])
            res += sum(1 for k, v in freq.items() if v == 1)
    return res


for s in inputs:
    print(main(s))

print()


# T=n,S=n
def main(s):
    res = 0
    charToIndexList = defaultdict(list)
    for i, char in enumerate(s):
        charToIndexList[char].append(i)
    for indexList in charToIndexList.values():
        size = len(indexList)
        for i in range(size):
            left = (indexList[i] - 0) if i == 0 else indexList[i] - (indexList[i - 1] + 1)
            right = ((len(s) - 1) - indexList[i]) if i == size - 1 else (indexList[i + 1] - 1) - indexList[i]
            res += (1 + left + right + left * right)
    return res


for s in inputs:
    print(main(s))
