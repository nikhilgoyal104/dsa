from collections import deque


def valid(s):
    bal = 0
    for char in s:
        if char == '(':
            bal += 1
        elif char == ')':
            bal -= 1
        if bal < 0:
            return False
    return not bal


def removeCount(s):
    n = len(s)
    stack = []
    countToRemove = 0
    for i in range(n):
        if s[i] != ')':
            stack.append(i)
        else:
            while stack and s[stack[-1]] != '(':
                stack.pop()
            if not stack:
                countToRemove += 1
            else:
                stack.pop()
    return countToRemove + sum(1 for i in stack if s[i] == '(')


# T=2ⁿ,S=n
def x(s):
    n = len(s)
    res = []
    vis = set()
    k = removeCount(s)
    queue = deque([(s, k)])
    vis.add(s)
    while queue:
        s, k = queue.popleft()
        if not k and valid(s):
            res.append(s)
            continue
        for i in range(len(s)):
            nbr = s[:i] + s[i + 1:]
            if nbr not in vis:
                vis.add(nbr)
                queue.append((nbr, k - 1))
    return res


# T=2ⁿ,S=n
def y(s):
    n = len(s)
    res = []
    vis = set()
    k = removeCount(s)

    def dfs(s, k):
        if not k:
            if valid(s):
                res.append(s)
            return
        for i in range(len(s)):
            nbr = s[:i] + s[i + 1:]
            if nbr not in vis:
                vis.add(nbr)
                dfs(nbr, k - 1)

    dfs(s, k)
    return res


for s in [
    '((()((s((((()',
    '()())()',
    '(a)())()',
    ')('
]:
    print(x(s), end=' ')
    print(y(s))
