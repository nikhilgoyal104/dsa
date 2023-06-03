# T=n,S=n
def main(s):
    stack = []
    openBracketToCloseBracketMap = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    def isAnOpeningBracket(char):
        return char in openBracketToCloseBracketMap

    def getClosingBracket(char):
        return openBracketToCloseBracketMap.get(char)

    for char in s:
        if isAnOpeningBracket(char):
            stack.append(char)
        else:
            top = stack.pop() if stack else ''
            if char != getClosingBracket(top):
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
