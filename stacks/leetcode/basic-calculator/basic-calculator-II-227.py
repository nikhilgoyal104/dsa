def priority(operator):
    if operator in ['+', '-']:
        return 1
    if operator in ['/', '*']:
        return 2
    return 0


def apply(operator, num2, num1):
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
        else:
            while operators and priority(operators[-1]) >= priority(s[i]):
                nums.append(apply(operators.pop(), nums.pop(), nums.pop()))
            operators.append(s[i])
        i += 1
    while operators:
        nums.append(apply(operators.pop(), nums.pop(), nums.pop()))
    return nums.pop()


for s in [
    '2*5/2',
    '3+2*2',
    ' 3/2 ',
    ' 3+5 / 2 '
]:
    print(str(s) + '->' + str(main(s)))
