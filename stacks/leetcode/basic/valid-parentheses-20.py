# T=n,S=n
def main(s):
    stack, mapping = [], {'(': ')', '{': '}', '[': ']'}
    for char in s:
        if char in mapping:
            stack.append(char)
        else:
            top = stack.pop() if stack else ''
            if char != mapping.get(top, ''):
                return False
    return not stack


for s in [
    '[',
    '))))',
    '[}',
    '(()',
    '()',
    '()[]{}',
    '(]',
    '([)]',
    '{[]}',
    ']',
    '(])'
]:
    print(s + ' -> ' + str(main(s)))
