# T=n,S=n
def x(s):
    stack = []
    for char in s:
        if char != ')':
            stack.append(char)
        else:
            if stack[-1] == '(':
                return True
            while stack and stack[-1] != '(':
                stack.pop()
            stack.pop()
    return False


for s in [
    '(a)', '()', '(a+b)', '((a+b))', '((a+b)+((c+d)))', '((a+b)+(c+d))'
]:
    print(x(s))
