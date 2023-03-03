# T=n,S=n
def main(s):
    stack = []
    close = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for char in s:
        if char in close:
            stack.append(char)
            continue
        bracket = stack.pop() if stack else ''
        if char != close.get(bracket):
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
