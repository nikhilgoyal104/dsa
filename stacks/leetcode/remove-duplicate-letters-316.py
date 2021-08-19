from collections import Counter


# T=n,S=1
def x(s):
    frequency, stack = Counter(s), []
    for char in s:
        frequency[char] -= 1
        if char not in stack:
            while stack and stack[-1] > char and frequency[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
    return ''.join(stack)


# T=n,S=1
def y(s):
    lastOccurence, stack = {char: i for i, char in enumerate(s)}, []
    for i, char in enumerate(s):
        if char not in stack:
            while stack and stack[-1] > char and i < lastOccurence[stack[-1]]:
                stack.pop()
            stack.append(char)
    return ''.join(stack)


for s in [
    'aaa',
    'abacb',
    'bcabc',
    'cbacdcbc',
    'cdadabcc',
    'bbcaac',
    'cbeacdcbc',
    'bcbac'
]:
    print(x(s), end=' ')
    print(y(s))
