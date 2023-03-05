def priority(operator):
    map = {
        '+': 1,
        '-': 1
    }
    return map.get(operator, 0)


def compute(operator, num2, num1):
    map = {
        '+': num1 + num2,
        '-': num1 - num2
    }
    return map[operator]


# T=n,S=n
def main(s):
    s = s.replace(' ', '')
    if s[0] == '-':
        s = '0' + s
    n = len(s)
    i = 0
    nums = []
    operators = []
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
                nums.append(compute(operators.pop(), nums.pop(), nums.pop()))
            operators.pop()
        else:
            while operators and priority(operators[-1]) >= priority(s[i]):
                nums.append(compute(operators.pop(), nums.pop(), nums.pop()))
            operators.append(s[i])
        i += 1
    while operators:
        nums.append(compute(operators.pop(), nums.pop(), nums.pop()))
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
