# T=n,S=n
def main(s):
    stack = []
    openToCloseMap = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for char in s:
        if char in openToCloseMap:
            stack.append(char)
            continue
        bracket = stack.pop() if stack else ''
        if char != openToCloseMap.get(bracket):
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
