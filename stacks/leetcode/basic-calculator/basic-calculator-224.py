def priority(operator):
    if operator in ['+', '-']:
        return 1
    return 0


def apply(operator, num2, num1):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2


# T=n,S=n
def main(s):
    s = s.replace(' ', '')
    if s[0] == '-':
        s = '0' + s
    i, n = 0, len(s)
    nums, operators = [], []
    while i < n:
        if s[i].isdigit():
            num = 0
            while i < n and s[i].isdigit():
                num = 10 * num + int(s[i])
                i += 1
            nums.append(num)
            i -= 1
        elif s[i] == '(':
            operators.append('(')
        elif s[i] == ')':
            while operators and operators[-1] != '(':
                nums.append(apply(operators.pop(), nums.pop(), nums.pop()))
            operators.pop()
        else:
            while operators and priority(operators[-1]) >= priority(s[i]):
                nums.append(apply(operators.pop(), nums.pop(), nums.pop()))
            operators.append(s[i])
        i += 1
    while operators:
        nums.append(apply(operators.pop(), nums.pop(), nums.pop()))
    return nums.pop()


for s in [
    '(7)-(0)+(4)',
    '-2+ 1',
    '7-8+9',
    '(7-(8+9))',
    '1 + 1',
    ' 2-1 + 2 ',
    '(1+(4+5+2)-3)+(6+8)'
]:
    print(str(s) + '->' + str(main(s)))
