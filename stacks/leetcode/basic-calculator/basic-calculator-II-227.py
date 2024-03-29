def priority(operator):
    map = {
        '+': 1,
        '-': 1,
        '/': 2,
        '*': 2
    }
    return map[operator]


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
        else:
            while operators and priority(operators[-1]) >= priority(s[i]):
                nums.append(compute(operators.pop(), nums.pop(), nums.pop()))
            operators.append(s[i])
        i += 1
    while operators:
        nums.append(compute(operators.pop(), nums.pop(), nums.pop()))
    return nums.pop()


for s in [
    '2*5/2',
    '3+2*2',
    ' 3/2 ',
    ' 3+5 / 2 ',
    '0+0',
    '123+431-431'
]:
    print(str(s) + '->' + str(main(s)))
