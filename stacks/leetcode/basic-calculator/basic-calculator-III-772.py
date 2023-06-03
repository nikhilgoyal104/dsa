def priority(operator):
    map = {
        '+': 1,
        '-': 1,
        '/': 2,
        '*': 2
    }
    return map.get(operator, 0)


def compute(operator, num2, num1):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        return int(num1 / num2)


# T=n,S=n
def main(s):
    s = s.replace(' ', '')
    i = 0
    nums = []
    operators = []
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
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
    '(5-12)/2',
    '(0-3)/4',
    '1+1',
    '6-4/2',
    '2*(5+5*2)/3+(6/2+8)',
    '(2+6*3+5-(3*14/7+2)*5)+3',
    '0',
]:
    print(str(s) + '->' + str(main(s)))
