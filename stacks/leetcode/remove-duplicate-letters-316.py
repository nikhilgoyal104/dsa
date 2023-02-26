from collections import Counter

inputs = [
    'aaa',
    'abacb',
    'bcabc',
    'cbacdcbc',
    'cdadabcc',
    'bbcaac',
    'cbeacdcbc',
    'bcbac'
]


# T=n,S=1
def main(s):
    stack = []
    freq = Counter(s)
    for char in s:
        freq[char] -= 1
        if char not in stack:
            while stack and stack[-1] > char and freq[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
    return ''.join(stack)


for s in inputs:
    print(main(s), end=' ')

print()


# T=n,S=1
def main(s):
    stack = []
    lastOccurence = {char: i for i, char in enumerate(s)}
    for i, char in enumerate(s):
        if char not in stack:
            while stack and stack[-1] > char and i < lastOccurence[stack[-1]]:
                stack.pop()
            stack.append(char)
    return ''.join(stack)


for s in inputs:
    print(main(s), end=' ')
