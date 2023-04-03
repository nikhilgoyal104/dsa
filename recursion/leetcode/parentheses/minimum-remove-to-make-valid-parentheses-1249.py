# T=n,S=n
def main(s):
    n = len(s)
    stack = []
    indicesToRemove = set()
    for i in range(n):
        if s[i] != ')':
            stack.append(i)
        else:
            while stack and s[stack[-1]] != '(':
                stack.pop()
            if not stack:
                indicesToRemove.add(i)
            else:
                stack.pop()
    indicesToRemove.update({i for i in stack if s[i] == '('})
    return ''.join(s[i] for i in range(n) if i not in indicesToRemove)


for s in [
    'lee(t(c)o)de)',
    'a)b(c)d',
    '))((',
    '(a(b(c)d)'
]:
    print(main(s))
