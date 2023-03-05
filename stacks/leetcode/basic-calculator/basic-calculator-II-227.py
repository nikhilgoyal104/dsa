def priority(operator):
    map = {
        '+': 1,
        '-': 1,
        '/': 2,
        '*': 2
    }
    return map[operator]


def compute(operator, num2, num1):
    map = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': int(num1 / num2)
    }
    return map[operator]


# T=n,S=n
def main(s):
    s = s.replace(' ', '')
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
    ' 3+5 / 2 '
]:
    print(str(s) + '->' + str(main(s)))
